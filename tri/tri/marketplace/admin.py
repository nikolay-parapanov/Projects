from django.contrib.auth import get_user_model
from django.contrib import admin

from tri.marketplace.models import MarketItems

UserModel = get_user_model()


@admin.register(MarketItems)
class MarketItems(admin.ModelAdmin):
    list_filter = ["name", "description", "price", "type", "user_id"]
    list_display = ["pk", "name", "description", "price", "type", "user_id"]
    search_fields = ["name", "description", "price", "type", "user_id"]
    ordering = ["pk"]


