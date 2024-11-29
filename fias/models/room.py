from django.db import models

from fias.fields import UUIDField

from .abstract_addrobj import AddrObjCommonMixin
from .room_type import RoomType

__all__ = ['Room']


class Room(AddrObjCommonMixin):
    """
    Классификатор помещений
    """

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    objectid = models.BigIntegerField('Глобальный уникальный идентификатор записи')

    objectguid = UUIDField('Глобальный уникальный идентификатор записи')

    changeid = models.BigIntegerField('ID изменившей транзакции')

    number = models.CharField('Номер комнаты или офиса', max_length=50)
    roomtype = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='+',
                                 db_column='roomtype',
                                 verbose_name='Тип комнаты или офиса')

    def __str__(self):
        return self.number
