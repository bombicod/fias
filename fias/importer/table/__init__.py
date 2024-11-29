import os
import re

from .table import BadTableError, tables_map

from .xml import XMLTable

table_xml_prefix = 'as_'
table_xml_pattern = r'(?P<deleted>del_)?(?P<name>[a-z_]+)_(?P<date>\d+)_(?P<uuid>[a-z0-9-]{36}).xml'
# table_dbf_pattern = r'(?P<deleted>D)?(?P<name>[a-z]+)(?P<seq>\d+)?.dbf'
# table_dbt_pattern = r'(?P<name>[a-z]+)(?P<seq>\d+)?.dbt'
table_xml_re = re.compile(table_xml_prefix + table_xml_pattern, re.I)


# table_dbf_re = re.compile(table_dbf_pattern, re.I)
# table_dbt_re = re.compile(table_dbt_pattern, re.I)


class BadTableNameError(Exception):
    pass


class TableFactory(object):

    @staticmethod
    def parse(filename):
        cls = None

        # Оставляем только имя самого файла
        basename = os.path.basename(filename)

        m = table_xml_re.match(basename)
        if m is not None:
            cls = XMLTable

        # m = table_dbf_re.match(filename)
        # if m is not None:
        #     cls = DBFTable
        #     return cls(filename=filename, **m.groupdict())
        #
        # m = table_dbt_re.match(filename)
        # if m is not None:
        #     return None

        if cls is not None:
            return cls(filename=filename, **m.groupdict())

        return None
