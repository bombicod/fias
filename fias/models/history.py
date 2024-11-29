from django.db import models
from fias.fields import UUIDField

from .operation_type import OperationType

__all__ = ['ChangeHistory']


# TODO: поля ID нет в таблице???
class ChangeHistory(models.Model):
    class Meta:
        verbose_name = 'Запись истории изменений'
        verbose_name_plural = 'Записи истории изменений'

    changeid = models.BigIntegerField('ID изменившей транзакции')
    objectid = models.BigIntegerField('Уникальный ID объекта')
    adrobjectid = UUIDField('Уникальный ID изменившей транзакции (GUID)')
    opertypeid = models.ForeignKey(OperationType, on_delete=models.CASCADE, related_name='+',
                                   db_column='opertypeid',
                                   verbose_name='Тип операции')
    ndocid = models.BigIntegerField('ID документа')
    changedate = models.DateField('Дата изменения')
