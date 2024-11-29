from django.db import models
from fias.fields import UUIDField

from .abstract_common import Param

__all__ = ['AddrObjParam']


class AddrObjParam(Param):
    class Meta:
        verbose_name = 'Параметр адресообразующих объектов'
        verbose_name_plural = 'Параметры адресообразующих объектов'
