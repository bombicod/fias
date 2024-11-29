from django.db import models
from .abstract_common import AddrObjRelevanceMixin, DatesMixin, LinkingMixin
from .operation_type import OperationType


class AddrObjCommonMixin(AddrObjRelevanceMixin, DatesMixin, LinkingMixin):
    class Meta:
        abstract = True

    opertypeid = models.ForeignKey(OperationType, on_delete=models.CASCADE, related_name='+',
                                   db_column='opertypeid',
                                   verbose_name='Статус действия',
                                   help_text='Статус действия над записью - причина появления записи')
