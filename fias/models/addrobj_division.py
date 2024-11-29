from django.db import models

__all__ = ['AddrObjDivision']


class AddrObjDivision(models.Model):
    class Meta:
        verbose_name = 'Операция переподчинения'
        verbose_name_plural = 'Операции переподчинения'

    parentid = models.BigIntegerField('Родительский ID')
    childid = models.BigIntegerField('Дочерний ID')

    changeid = models.BigIntegerField('ID изменившей транзакции')
