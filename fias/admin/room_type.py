from django.contrib import admin

from fias.models import RoomType


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'isactive')
