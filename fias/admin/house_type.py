from django.contrib import admin

from fias.models import HouseType


@admin.register(HouseType)
class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'isactive')
