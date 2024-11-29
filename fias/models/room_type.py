from django.db import models
from fias.fields import UUIDField

from .abstract_common import DatesMixin

__all__ = ['RoomType']


class RoomType(DatesMixin):
    class Meta:
        verbose_name = 'Тип комнаты'
        verbose_name_plural = 'Типы комнат'

    name = models.CharField('Наименование', max_length=100)
    shortname = models.CharField('Краткое наименование', max_length=50, blank=True)
    desc = models.CharField('Описание', max_length=250)

    isactive = models.BooleanField('Статус активности')

    def __str__(self):
        return self.name
