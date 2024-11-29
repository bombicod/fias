from django.db import models
from fias.fields import UUIDField

from .abstract_common import DatesMixin

__all__ = ['ObjectLevel']


class ObjectLevel(DatesMixin):
    class Meta:
        verbose_name = 'Уровень адресного объекта'
        verbose_name_plural = 'Уровни адресных объектов'

    level = models.IntegerField('Номер уровня объекта', primary_key=True,
                                help_text='Уникальный идентификатор записи. Ключевое поле.')

    name = models.CharField('Наименование', max_length=250)
    shortname = models.CharField('Краткое наименование', max_length=50, blank=True)

    isactive = models.BooleanField('Признак действующего адресного объекта')

    def __str__(self):
        return self.name
