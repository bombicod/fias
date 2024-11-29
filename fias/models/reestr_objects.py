from django.db import models
from fias.fields import UUIDField

__all__ = ['Object']


class Object(models.Model):
    class Meta:
        verbose_name = 'GUID-объект'
        verbose_name_plural = 'GUID-объекты'

    objectid = models.BigIntegerField('Уникальный идентификатор объекта')
    createdate = models.DateField('Дата создания')
    changeid = models.BigIntegerField('ID изменившей транзакции')
    levelid = models.IntegerField('Уровень объекта')
    updatedate = models.DateField('Дата обновления')
    objectguid = UUIDField('GUID объекта')
    isactive = models.IntegerField('Признак действующего объекта')
