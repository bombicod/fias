from django.contrib import admin

from fias.models import MunHierarchy


@admin.register(MunHierarchy)
class MunHierarchyAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'oktmo', 'isactive')
