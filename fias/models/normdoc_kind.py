from django.db import models
from fias.fields import UUIDField

__all__ = ['NDocKind']


class NDocKind(models.Model):
    class Meta:
        verbose_name = 'Вид нормативного документа'
        verbose_name_plural = 'Виды нормативных документов'

    name = models.CharField('Наименование', max_length=500)

    def __str__(self):
        return self.name
