from django.db import models
from fias.fields import UUIDField

from .abstract_common import (
    ActiveChoices,
    DatesMixin,
    LinkingMixin
)

__all__ = ['AdmHierarchy']

# TODO: USE Treebeard?
class AdmHierarchy(DatesMixin, LinkingMixin):
    class Meta:
        verbose_name = 'Запись иерархии административного деления'
        verbose_name_plural = 'Записи иерархии административного деления'

    # AddrObj
    objectid = models.BigIntegerField('Глобальный уникальный идентификатор объекта')
    parentobjid = models.BigIntegerField('Идентификатор родительского объекта', blank=True, null=True)

    # ChangeHistory
    changeid = models.BigIntegerField('ID изменившей транзакции')
    regioncode = models.CharField('Код региона', max_length=4, blank=True)
    areacode = models.CharField('Код района', max_length=4, blank=True)
    citycode = models.CharField('Код города', max_length=4, blank=True)
    placecode = models.CharField('Код населённого пункта', max_length=4, blank=True)
    plancode = models.CharField('Код ЭПС', max_length=4, blank=True)
    streetcode = models.CharField('Код улицы', max_length=4, blank=True)

    isactive = models.SmallIntegerField('Признак действующего адресного объекта',
                                        choices=ActiveChoices.choices)

    path = models.CharField('Материализованный путь к объекту', max_length=300)
