from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AuctionItem
from .serializers import AuctionItemSerializer, AuctionItemCreateSerializer, BidSerializer
from rest_framework.permissions import IsAuthenticated

# List all active auction items with optional filters
class AuctionItemListView(generics.ListAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply filters for category and price range if provided
        category = self.request.query_params.get('category')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if category:
            queryset = queryset.filter(category_id=category)
        if min_price:
            queryset = queryset.filter(current_price__gte=min_price)
        if max_price:
            queryset = queryset.filter(current_price__lte=max_price)
        return queryset

# Get details of a specific auction item
class AuctionItemDetailView(generics.RetrieveAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer
    lookup_field = 'id'

# Place a new bid on an item
class PlaceBidView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = BidSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auction_item_id = serializer.validated_data['auction_item_id']
        bid_amount = serializer.validated_data['bid_amount']

        try:
            auction_item = AuctionItem.objects.get(id=auction_item_id)
            if bid_amount <= auction_item.current_price:
                return Response({"error": "Bid must be higher than the current price."}, status=status.HTTP_400_BAD_REQUEST)
            auction_item.current_price = bid_amount
            auction_item.save()
            return Response({"success": "Bid placed successfully."})
        except AuctionItem.DoesNotExist:
            return Response({"error": "Auction item not found."}, status=status.HTTP_404_NOT_FOUND)

# Create a new auction item
class AuctionItemCreateView(generics.CreateAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemCreateSerializer
    permission_classes = [IsAuthenticated]

# Update details of an existing auction item
class AuctionItemUpdateView(generics.UpdateAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

# Delete an auction item
class AuctionItemDeleteView(generics.DestroyAPIView):
    queryset = AuctionItem.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
