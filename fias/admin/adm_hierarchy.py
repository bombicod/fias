from django.contrib import admin

from fias.models import AdmHierarchy


@admin.register(AdmHierarchy)
class AdmHierarchyAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'regioncode', 'areacode', 'citycode', 'placecode', 'plancode', 'streetcode', 'isactive')
