from django.contrib import admin

from fias.models import ApartmentType


@admin.register(ApartmentType)
class ApartmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'isactive')
