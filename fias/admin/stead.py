from django.contrib import admin

from fias.models import Stead


@admin.register(Stead)
class SteadAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'number', 'isactual', 'isactive')
