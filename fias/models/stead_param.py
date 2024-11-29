from django.db import models
from fias.fields import UUIDField

from .abstract_common import Param

__all__ = ['SteadParam']


class SteadParam(Param):
    class Meta:
        verbose_name = 'Параметр земельных участков'
        verbose_name_plural = 'Параметры земельных участков'
