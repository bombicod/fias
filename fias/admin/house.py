from django.contrib import admin

from fias.models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'housenum', 'addnum1', 'addnum2', 'isactual', 'isactive')
