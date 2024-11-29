from django.db import models
from fias.fields import UUIDField

from .abstract_common import DatesMixin, LinkingMixin

__all__ = ['HouseType']


class HouseType(DatesMixin):
    class Meta:
        verbose_name = 'Тип дома'
        verbose_name_plural = 'Типы домов'

    name = models.CharField('Наименование', max_length=50)
    shortname = models.CharField('Краткое наименование', max_length=50, blank=True)
    desc = models.CharField('Описание', max_length=250, blank=True)

    isactive = models.BooleanField('Статус активности')

    def __str__(self):
        return self.name
