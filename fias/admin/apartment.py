from django.contrib import admin

from fias.models import Apartment


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'number', 'aparttype', 'isactual', 'isactive')
