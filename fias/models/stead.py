from django.db import models

from fias.fields import UUIDField

from .abstract_addrobj import AddrObjCommonMixin

__all__ = ['Stead']


class Stead(AddrObjCommonMixin):
    """
    Сведения о земельных участках
    """

    class Meta:
        verbose_name = 'Земельный участок'
        verbose_name_plural = 'Земельные участки'

    objectid = models.BigIntegerField('Глобальный уникальный идентификатор объекта')
    objectguid = UUIDField('Глобальный уникальный идентификатор объекта')

    changeid = models.BigIntegerField('ID изменившей транзакции')

    number = models.CharField('Номер земельного участка', max_length=250)

    def __str__(self):
        return self.number
