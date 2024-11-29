from django.contrib import admin

from fias.models import RoomParam


@admin.register(RoomParam)
class RoomParamAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'typeid', 'value')
