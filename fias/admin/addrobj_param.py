from django.contrib import admin

from fias.models import AddrObjParam


@admin.register(AddrObjParam)
class AddrObjParamAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'typeid', 'value')
