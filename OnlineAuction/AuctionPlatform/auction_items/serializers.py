from rest_framework import serializers
from .models import AuctionItem

class AuctionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionItem
        fields = '__all__'
        read_only_fields = ['current_price', 'created_at']

class AuctionItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionItem
        fields = ['title', 'description', 'starting_price', 'end_date', 'category']

class BidSerializer(serializers.Serializer):
    auction_item_id = serializers.IntegerField()
    bid_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
