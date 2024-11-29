from django.contrib import admin

from fias.models import NDocKind


@admin.register(NDocKind)
class NormDocAdmin(admin.ModelAdmin):
    list_display = ('name',)
