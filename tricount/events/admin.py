from django.contrib import admin

from tricount.events.models import Event


@admin.register(Event)
class PropertyPhotoAdmin(admin.ModelAdmin):
    list_display = ["user", "label", "settle", "started_at", "ended_at", "created_at"]
    list_filter = ["user", "started_at", "ended_at", "created_at", "settle"]
