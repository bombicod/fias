from django.db import models
from fias.fields import UUIDField

from .abstract_common import Param

__all__ = ['HouseParam']


class HouseParam(Param):
    class Meta:
        verbose_name = 'Параметр дома'
        verbose_name_plural = 'Параметры домов'
