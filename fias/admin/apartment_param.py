from django.contrib import admin

from fias.models import ApartmentParam


@admin.register(ApartmentParam)
class ApartmentParamAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'typeid', 'value')
