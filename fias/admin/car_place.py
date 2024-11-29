from django.contrib import admin

from fias.models import CarPlace


@admin.register(CarPlace)
class CarPlaceAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'number', 'isactual', 'isactive')
