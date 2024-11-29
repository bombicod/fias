from django.db import models

from fias.fields import UUIDField

from .abstract_addrobj import AddrObjCommonMixin

__all__ = ['AddrObj']


class AddrObj(AddrObjCommonMixin):
    """
    Классификатор адресообразующих элементов
    """

    class Meta:
        verbose_name = 'Адресообразующий элемент'
        verbose_name_plural = 'Адресообразующие элементы'
        # index_together = (
        #
        # )
        # ordering = ['aolevel', 'formalname']

    objectid = models.BigIntegerField('Глобальный уникальный идентификатор адресного объекта', db_index=True)
    objectguid = UUIDField('Глобальный уникальный идентификатор адресного объекта', db_index=True)
    changeid = models.BigIntegerField('Изменившая транзакция')

    name = models.CharField('Наименование', max_length=250)
    typename = models.CharField('Краткое наименование', max_length=50)

    level = models.CharField('Уровень адресного объекта', max_length=10, db_index=True)



    def full_name(self, depth=None, formal=False):
        assert isinstance(depth, int), 'Depth must be integer'

        if not self.parentguid or self.aolevel <= 1 or depth <= 0:
            if formal:
                return self.get_formal_name()
            return self.get_natural_name()
        else:
            parent = AddrObj.objects.get(pk=self.parentguid)
            return '{0}, {1}'.format(parent.full_name(depth - 1, formal), self)

    def get_natural_name(self):
        if self.aolevel == 1:
            return '{0} {1}'.format(self.formalname, self.shortname)
        return self.get_formal_name()

    def get_formal_name(self):
        return '{0} {1}'.format(self.typename, self.name)

    def __str__(self):
        return self.get_formal_name()

    def full_address(self):
        return self.full_name(5)
