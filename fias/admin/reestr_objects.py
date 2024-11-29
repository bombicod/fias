from django.contrib import admin

from fias.models import Object


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'createdate', 'levelid', 'isactive')
