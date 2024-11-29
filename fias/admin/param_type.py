from django.contrib import admin

from fias.models import ParamType


@admin.register(ParamType)
class ParamTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'isactive')
