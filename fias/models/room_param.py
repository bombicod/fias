from django.db import models
from fias.fields import UUIDField

from .abstract_common import Param

__all__ = ['RoomParam']


class RoomParam(Param):
    class Meta:
        verbose_name = 'Параметр помещения'
        verbose_name_plural = 'Параметры помещений'
