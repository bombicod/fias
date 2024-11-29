from django.db import models

from fias.fields import UUIDField

from .abstract_common import DatesMixin

__all__ = ['AddrObjType']


class AddrObjType(DatesMixin):
    class Meta:
        verbose_name = 'Тип адресного объекта'
        verbose_name_plural = 'Типы адресных объектов'

    level = models.IntegerField('Уровень адресного объекта')
    shortname = models.CharField('Краткое наименование типа объекта', max_length=50)
    name = models.CharField('Полное наименование типа объекта', max_length=250)

    desc = models.CharField('Описание', max_length=250, blank=True)

    isactive = models.BooleanField('Статус активности')

    def __str__(self):
        return self.name
