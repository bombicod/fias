from django.db import models
from django.db.models.enums import IntegerChoices
from django.utils.translation import gettext_lazy as _
from fias.fields import UUIDField


class ActualChoices(IntegerChoices):
    ACTUAL = 1, _('Actual')
    NOT_ACTUAL = 0, _('Not actual')


class ActiveChoices(IntegerChoices):
    ACTIVE = 1, _('Active')
    NOT_ACTIVE = 0, _('Not active')


class DatesMixin(models.Model):
    class Meta:
        abstract = True

    updatedate = models.DateField('Дата внесения (обновления) записи')
    startdate = models.DateField('Начало действия записи')
    enddate = models.DateField('Окончание действия записи')


class LinkingMixin(models.Model):
    class Meta:
        abstract = True

    previd = models.BigIntegerField('Идентификатор записи связывания с предыдущей исторической записью')
    nextid = models.BigIntegerField('Идентификатор записи связывания с последующей исторической записью')


class AddrObjRelevanceMixin(models.Model):
    class Meta:
        abstract = True

    isactual = models.IntegerField('Статус актуальности',
                                   choices=ActualChoices.choices)
    isactive = models.IntegerField('Признак действующего адресного объекта',
                                   choices=ActiveChoices.choices)


class Param(DatesMixin):
    class Meta:
        verbose_name = 'Параметр адресообразующих объектов и объектов недвижимости'
        verbose_name_plural = 'Параметры адресообразующих объектов и объектов недвижимости'
        abstract = True

    objectid = models.BigIntegerField('Глобальный уникальный идентификатор адресного объекта')
    changeid = models.BigIntegerField('ID изменившей транзакции', blank=True, null=True)
    changeidend = models.BigIntegerField('ID завершившей транзакции')
    typeid = models.IntegerField('Тип параметра')
    value = models.TextField('Значение параметра', max_length=8000)

    def __str__(self):
        return self.value
