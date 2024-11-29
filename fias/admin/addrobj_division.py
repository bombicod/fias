from django.contrib import admin

from fias.models import AddrObjDivision


@admin.register(AddrObjDivision)
class AddrObjDivisionAdmin(admin.ModelAdmin):
    list_display = ('parentid', 'childid', 'changeid')
