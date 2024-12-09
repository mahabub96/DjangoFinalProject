from django.contrib import admin
from .models import AuctionItem

class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'current_price', 'end_date', 'category', 'user', 'created_at')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('category', 'end_date')
    ordering = ('-created_at',)

admin.site.register(AuctionItem, AuctionItemAdmin)
