from django.db import models
from fias.fields import UUIDField

__all__ = ['NDocType']


class NDocType(models.Model):
    class Meta:
        verbose_name = 'Тип нормативного документа'
        verbose_name_plural = 'Типы нормативных документов'

    name = models.CharField('Наименование', max_length=500)

    startdate = models.DateField('Дата начала действия')
    enddate = models.DateField('Дата окончания действия')

    def __str__(self):
        return self.name
