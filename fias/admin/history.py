from django.contrib import admin

from fias.models import ChangeHistory


@admin.register(ChangeHistory)
class ChangeHistoryAdmin(admin.ModelAdmin):
    list_display = ('changeid', 'objectid', 'adrobjectid', 'changedate')
