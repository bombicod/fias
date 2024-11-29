import datetime
import logging

from django.conf import settings
from django import db
from django.db import IntegrityError
from sys import stderr

from .signals import (
    pre_import_table,
    post_import_table
)
from .validators import validators

logger = logging.getLogger(__name__)


class TableLoader:

    def __init__(self, limit=10000):
        self.limit = int(limit)
        self.counter = 0
        self.upd_counter = 0
        self.skip_counter = 0
        self.err_counter = 0
        self.today = datetime.date.today()

    def validate(self, table, item):
        if item is None or item.pk is None:
            return False

        return validators.get(table.name, lambda x, **kwargs: True)(item, today=self.today)

    def regressive_create(self, table, objects, bar, depth=1):
        count = len(objects)
        batch_len = count // 3 or 1
        batch_count = count // batch_len
        if batch_count * batch_len < count:
            batch_count += 1
        objects = list(objects)

        for i in range(0, batch_count):
            batch = objects[i * batch_len:(i + 1) * batch_len]
            # bar.update(regress_depth=depth, regress_len=batch_len, regress_iteration=i + 1)
            try:
                table.model.objects.bulk_create(batch)
            except (IntegrityError, ValueError) as e:
                if batch_len <= 1:
                    self.counter -= 1
                    self.skip_counter += 1
                    self.err_counter += 1
                    # bar.update(loaded=self.counter, skipped=self.skip_counter, errors=self.err_counter)
                    continue
                else:
                    self.regressive_create(table, batch, bar=bar, depth=depth + 1)

    def create(self, table, objects, bar):
        try:
            table.model.objects.bulk_create(objects)
        except (IntegrityError, ValueError):
            self.regressive_create(table, objects, bar)

        #  Обнуляем индикатор регрессии
        # bar.update(regress_depth=0, regress_len=0)
        if settings.DEBUG:
            db.reset_queries()

    def load(self, tablelist, table):
        pre_import_table.send(sender=self.__class__, table=table)
        self.do_load(tablelist=tablelist, table=table)
        post_import_table.send(sender=self.__class__, table=table)

    def do_load(self, tablelist, table):
        bar = None
        # bar = LoadingBar(table=table.name, filename=table.filename)
        # bar.update()

        # logger.debug(f'Loading: {tablelist}/{table}')
        print(f'Loading: {tablelist}/{table}')

        objects = set()
        for item in table.rows(tablelist=tablelist):
            if not self.validate(table, item):
                self.skip_counter += 1

                if self.skip_counter and self.skip_counter % self.limit == 0:
                    # bar.update(skipped=self.skip_counter)
                    pass
                continue

            objects.add(item)
            self.counter += 1

            if self.counter and self.counter % self.limit == 0:
                self.create(table, objects, bar=bar)
                objects.clear()
                # bar.update(loaded=self.counter, skipped=self.skip_counter)

        if objects:
            self.create(table, objects, bar=bar)

        # bar.update(loaded=self.counter, skipped=self.skip_counter)
        # bar.finish()


class TableUpdater(TableLoader):

    def __init__(self, limit=10000):
        self.upd_limit = 100
        super(TableUpdater, self).__init__(limit=limit)

    def do_load(self, tablelist, table):
        bar = None
        # bar = LoadingBar(table=table.name, filename=table.filename)

        model = table.model
        objects = set()
        for item in table.rows(tablelist=tablelist):
            if not self.validate(table, item):
                self.skip_counter += 1
                continue

            try:
                old_obj = model.objects.get(pk=item.pk)
            except model.DoesNotExist:
                objects.add(item)
                self.counter += 1
            else:
                if not hasattr(item, 'updatedate') or old_obj.updatedate < item.updatedate:
                    item.save()
                    self.upd_counter += 1

            if self.counter and self.counter % self.limit == 0:
                self.create(table, objects, bar=bar)
                objects.clear()
                # bar.update(loaded=self.counter)

            if self.upd_counter and self.upd_counter % self.upd_limit == 0:
                # bar.update(updated=self.upd_counter)
                pass

        if objects:
            self.create(table, objects, bar=bar)

        # bar.update(loaded=self.counter, updated=self.upd_counter, skipped=self.skip_counter)
        # bar.finish()
