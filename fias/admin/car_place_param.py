from django.contrib import admin

from fias.models import CarPlaceParam


@admin.register(CarPlaceParam)
class CarPlaceParamAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'typeid', 'value')
