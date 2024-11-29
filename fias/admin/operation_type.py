from django.contrib import admin

from fias.models import OperationType


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'isactive')
