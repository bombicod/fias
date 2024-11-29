from django.db import connections, router, models

# from fias.config import TABLE_ROW_FILTERS
from fias.models import *

from typing import Iterator, Type

tables_map = {
    # Простые справочники
    'addr_obj_types': AddrObjType,
    'apartment_types': ApartmentType,
    'house_types': HouseType,
    'normative_docs_types': NDocType,
    'operation_types': OperationType,
    'param_types': ParamType,

    'addr_obj': AddrObj,
    'addr_obj_division': AddrObjDivision,
    'addr_obj_params': AddrObjParam,

    'adm_hierarchy': AdmHierarchy,
    'apartments': Apartment,
    'apartments_params': ApartmentParam,

    'carplaces': CarPlace,
    'carplaces_params': CarPlaceParam,

    'change_history': ChangeHistory,

    'houses': House,
    'houses_params': HouseParam,

    'mun_hierarchy': MunHierarchy,
    'normative_docs': NormDoc,
    'normative_docs_kinds': NDocKind,

    'object_levels': ObjectLevel,

    'reestr_objects': Object,
    'room_types': RoomType,
    'rooms': Room,
    'rooms_params': RoomParam,

    'steads': Stead,
    'steads_params': SteadParam,
}

name_trans = {

}


class BadTableError(Exception):
    pass


class ParentLookupException(Exception):
    pass


class TableIterator:

    def __init__(self, fd, model):
        self._fd = fd
        self.model = model

    def __iter__(self):
        if self.model is None:
            return []

        return self

    def get_context(self):
        raise NotImplementedError()

    def get_next(self):
        raise NotImplementedError()

    def format_row(self, row):
        raise NotImplementedError()

    def process_row(self, row):
        try:
            row = dict(self.format_row(row))
        except ParentLookupException as e:
            return None

        item = self.model(**row)

        # Убираем пока фильтрацию строк
        # for filter_func in TABLE_ROW_FILTERS.get(self.model._meta.model_name, tuple()):
        #     item = filter_func(item)
        #
        #     if item is None:
        #         break

        return item

    def __next__(self):
        return self.get_next()

    next = __next__


class Table(object):
    name: str
    deleted: bool = False
    iterator_class: Type[TableIterator]

    model: Type[models.Model]

    def __init__(self, filename, **kwargs):
        assert hasattr(self, 'iterator_class'), 'iterator_class must be set!'

        self.filename = filename

        name = kwargs['name'].lower()

        self.name = name_trans.get(name, name)
        self.model = tables_map.get(self.name)

        self.deleted = bool(kwargs.get('deleted', False))

    def _truncate(self, model: Type[models.Model]):
        db_table = model._meta.db_table
        connection = connections[router.db_for_write(model)]
        cursor = connection.cursor()

        if connection.vendor == 'postgresql':
            cursor.execute('TRUNCATE TABLE {0} RESTART IDENTITY CASCADE'.format(db_table))
        elif connection.vendor == 'mysql':
            cursor.execute('TRUNCATE TABLE `{0}`'.format(db_table))
        else:
            cursor.execute('DELETE FROM {0}'.format(db_table))

    def truncate(self):
        self._truncate(self.model)

    def open(self, tablelist):
        return tablelist.open(self.filename)

    def rows(self, tablelist) -> Iterator[models.Model]:
        raise NotImplementedError()

    def __repr__(self):
        return f'<{self.__class__.__name__}:{self.name} "{self.filename}">'
