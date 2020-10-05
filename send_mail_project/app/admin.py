from django.contrib import admin
from .models import Message

admin.site.site_title = "Почта"
admin.site.site_header = "Почта"

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "message")
    list_display_links = ("address",)
    list_filter = ("address",)
    search_fields = ("address",)