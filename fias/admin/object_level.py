from django.contrib import admin

from fias.models import ObjectLevel


@admin.register(ObjectLevel)
class ObjectLevelAdmin(admin.ModelAdmin):
    list_display = ('shortname', 'level', 'isactive')
