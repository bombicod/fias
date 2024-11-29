from django.db import models
from fias.fields import UUIDField

from .abstract_common import (
    ActiveChoices,
    DatesMixin,
    LinkingMixin
)

__all__ = ['MunHierarchy']


class MunHierarchy(DatesMixin, LinkingMixin):
    class Meta:
        verbose_name = 'Запись иерархии в муниципальном делении'
        verbose_name_plural = 'Записи иерархии в муниципальном делении'

    objectid = models.BigIntegerField('Глобальный уникальный идентификатор адресного объекта')
    parentobjid = models.BigIntegerField('Идентификатор родительского объекта')
    changeid = models.BigIntegerField('ID изменившей транзакции')

    oktmo = models.CharField('ОКТМО', max_length=11, blank=True)

    isactive = models.IntegerField('Признак действующего адресного объекта',
                                   choices=ActiveChoices.choices)

    path = models.CharField('Материализованный путь к объекту', max_length=300)
