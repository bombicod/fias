from django.db import models

from .abstract_common import DatesMixin

__all__ = ['OperationType']


class OperationType(DatesMixin):
    class Meta:
        verbose_name = 'Статус действия'
        verbose_name_plural = 'Статусы действий'

    name = models.CharField('Наименование', max_length=100)
    shortname = models.CharField('Краткое наименование', max_length=100, blank=True)
    desc = models.CharField('Описание', max_length=250, blank=True)

    isactive = models.BooleanField('Статус активности')

    def __str__(self):
        return self.name
