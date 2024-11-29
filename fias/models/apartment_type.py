from django.db import models
from fias.fields import UUIDField

from .abstract_common import DatesMixin

__all__ = ['ApartmentType']


class ApartmentType(DatesMixin):
    class Meta:
        verbose_name = 'Тип помещения'
        verbose_name_plural = 'Типы помещений'

    name = models.CharField('Наименование', max_length=50)
    shortname = models.CharField('Краткое наименование', max_length=50, blank=True)
    desc = models.CharField('Описание', max_length=250, blank=True)

    isactive = models.BooleanField('Статус активности')

    def __str__(self):
        return self.name
