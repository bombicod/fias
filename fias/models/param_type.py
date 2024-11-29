from django.db import models
from fias.fields import UUIDField

from .abstract_common import DatesMixin

__all__ = ['ParamType']


class ParamType(DatesMixin):
    class Meta:
        verbose_name = 'Тип параметра'
        verbose_name_plural = 'Типы параметров'

    name = models.CharField('Наименование', max_length=50)
    code = models.CharField('Краткое наименование', max_length=50)
    desc = models.CharField('Описание', max_length=120)

    isactive = models.BooleanField('Статус активности')

    def __str__(self):
        return self.name
