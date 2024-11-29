from django.contrib import admin

from fias.models import SteadParam


@admin.register(SteadParam)
class SteadParamAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'typeid', 'value')
