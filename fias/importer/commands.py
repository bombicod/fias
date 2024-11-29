import logging
import os
from django.db.models import Min
from fias.config import TABLES
from fias.models import Status, Version

from .indexes import remove_indexes_from_model, restore_indexes_for_model
from .signals import (
    pre_drop_indexes,
    post_drop_indexes,
    pre_restore_indexes,
    post_restore_indexes,
    pre_import,
    post_import,
    pre_update,
    post_update
)
from .source import *
from .table import BadTableError, tables_map
from .loader import TableLoader, TableUpdater

logger = logging.getLogger(__name__)


def get_table_list(path, version=None, data_format='gar', tempdir=None):
    assert data_format in ['gar', 'xml', 'dbf'], \
        'Unsupported data format: `{0}`. Available choices: {1}'.format(data_format, ', '.join(['xml', 'dbf']))

    if path is None:
        latest_version = Version.objects.latest('dumpdate')
        url = getattr(latest_version, 'complete_{0}_url'.format(data_format))

        tablelist = RemoteArchiveTableList(src=url, version=latest_version, tempdir=tempdir)

    else:
        if os.path.isfile(path):
            tablelist = LocalArchiveTableList(src=path, version=version, tempdir=tempdir)

        elif os.path.isdir(path):
            tablelist = DirectoryTableList(src=path, version=version, tempdir=tempdir)

        elif path.startswith('http://') or path.startswith('https://') or path.startswith('//'):
            tablelist = RemoteArchiveTableList(src=path, version=version, tempdir=tempdir)

        else:
            raise TableListLoadingError('Path `{0}` is not valid table list source'.format(path))

    return tablelist


def load_complete_data(path=None,
                       data_format='xml',
                       truncate=False,
                       limit=10000, tables=None,
                       keep_indexes=False,
                       tempdir=None,
                       ):
    tablelist = get_table_list(path=path, data_format=data_format, tempdir=tempdir)

    pre_import.send(sender=object.__class__, version=tablelist.version)

    for table_name in tables_map.keys():
        if table_name not in tablelist.tables:
            print(f'Skipped table: {table_name}')
            continue

        try:
            st = Status.objects.get(table=table_name)
            if truncate:
                st.delete()
                raise Status.DoesNotExist()
        except Status.DoesNotExist:
            # Берём для работы любую таблицу с именем tbl
            first_table = tablelist.tables[table_name][0]
            print(f'Processing table: {first_table}')

            # Очищаем таблицу перед импортом
            if truncate:
                first_table.truncate()

            # Удаляем индексы из модели перед импортом
            if not keep_indexes:
                pre_drop_indexes.send(sender=object.__class__, table=first_table)
                remove_indexes_from_model(model=first_table.model)
                post_drop_indexes.send(sender=object.__class__, table=first_table)

            # Импортируем все таблицы модели
            for table in tablelist.tables[table_name]:
                loader = TableLoader(limit=limit)
                loader.load(tablelist=tablelist, table=table)

            # Восстанавливаем удалённые индексы
            if not keep_indexes:
                pre_restore_indexes.send(sender=object.__class__, table=first_table)
                restore_indexes_for_model(model=first_table.model)
                post_restore_indexes.send(sender=object.__class__, table=first_table)

            st = Status(table=table_name, ver=tablelist.version)
            st.save()
        else:
            logger.warning('Table `{0}` has version `{1}`. '
                           'Please use --truncate for replace '
                           'all table contents. Skipping...'.format(st.table, st.ver))

    post_import.send(sender=object.__class__, version=tablelist.version)
