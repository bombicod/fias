from django.db import models
from fias.fields import UUIDField

from .abstract_addrobj import AddrObjCommonMixin

__all__ = ['CarPlace']


class CarPlace(AddrObjCommonMixin):
    class Meta:
        verbose_name = 'Машино-место'
        verbose_name_plural = 'Машино-места'

    objectid = models.BigIntegerField('Глобальный уникальный идентификатор объекта')
    objectguid = UUIDField('Глобальный уникальный идентификатор объекта')

    changeid = models.BigIntegerField('ID изменившей транзакции')

    number = models.CharField('Номер машиноместа', max_length=50)

    def __str__(self):
        return self.number
