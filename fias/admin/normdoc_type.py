from django.contrib import admin

from fias.models import NDocType


@admin.register(NDocType)
class NormDocAdmin(admin.ModelAdmin):
    list_display = ('name', 'startdate', 'enddate')
