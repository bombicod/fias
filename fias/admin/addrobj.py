from django.contrib import admin

from fias.models import AddrObj


@admin.register(AddrObj)
class AddrObjAdmin(admin.ModelAdmin):
    list_display = ('name', 'typename', 'level', 'isactual', 'isactive')
