from django.db import models

from fias.fields import UUIDField

from .abstract_addrobj import AddrObjCommonMixin
from .house_type import HouseType

__all__ = ['House']


class House(AddrObjCommonMixin):
    """
    Сведения по номерам домов улиц городов и населенных пунктов
    """

    class Meta:
        verbose_name = 'Номер дома'
        verbose_name_plural = 'Номера домов'

    objectid = models.BigIntegerField('Глобальный уникальный идентификатор объекта')
    objectguid = UUIDField('Глобальный уникальный идентификатор объекта')

    changeid = models.BigIntegerField('ID изменившей транзакции')

    housenum = models.CharField('Основной номер дома', max_length=50, blank=True)
    addnum1 = models.CharField('Дополнительный номер дома 1', max_length=50, blank=True)
    addnum2 = models.CharField('Дополнительный номер дома 2', max_length=50, blank=True)

    housetype = models.ForeignKey(HouseType, on_delete=models.CASCADE, related_name='+',
                                  db_column='housetype', blank=True, null=True,
                                  verbose_name='Основной тип дома')
    addtype1 = models.IntegerField('Дополнительный тип дома 1', blank=True, null=True)
    addtype2 = models.IntegerField('Дополнительный тип дома 2', blank=True, null=True)
