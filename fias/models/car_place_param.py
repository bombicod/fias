from django.db import models
from fias.fields import UUIDField

from .abstract_common import Param

__all__ = ['CarPlaceParam']


class CarPlaceParam(Param):
    class Meta:
        verbose_name = 'Параметр машино-места'
        verbose_name_plural = 'Параметры машино-мест'
