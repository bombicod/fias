from django.contrib import admin

from fias.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'number', 'roomtype', 'isactual', 'isactive')
