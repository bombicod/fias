from django.db import models
from fias.fields import UUIDField

from .apartment_type import ApartmentType
from .abstract_addrobj import AddrObjCommonMixin

__all__ = ['Apartment']


class Apartment(AddrObjCommonMixin):
    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    objectid = models.BigIntegerField('Глобальный уникальный идентификатор объекта')
    objectguid = UUIDField('Глобальный уникальный идентификатор объекта')
    changeid = models.BigIntegerField('ID изменившей транзакции')
    number = models.CharField('Номер комнаты', max_length=50)

    aparttype = models.ForeignKey(ApartmentType, on_delete=models.CASCADE, related_name='+',
                                  verbose_name='Тип комнаты')

    def __str__(self):
        return self.number
