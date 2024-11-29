from django.contrib import admin

from fias.models import Version, Status


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('ver', 'dumpdate', 'date')
