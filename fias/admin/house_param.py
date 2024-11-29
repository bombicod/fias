from django.contrib import admin

from fias.models import HouseParam


@admin.register(HouseParam)
class HouseParamAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'typeid', 'value')
