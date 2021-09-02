from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Memory


@admin.register(Memory)
class MemoryAdmin(OSMGeoAdmin):
    model = Memory
    # readonly_fields = ['author']


