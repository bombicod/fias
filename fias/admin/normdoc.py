from django.contrib import admin

from fias.models import NormDoc


@admin.register(NormDoc)
class NormDocAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'number', 'updatedate')
