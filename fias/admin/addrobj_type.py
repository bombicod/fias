from django.contrib import admin

from fias.models import AddrObjType


@admin.register(AddrObjType)
class AddrObjTypeAdmin(admin.ModelAdmin):
    list_display = ('shortname', 'level', 'isactive')
