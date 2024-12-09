from django.urls import path
from .views import (
    AuctionItemListView,
    AuctionItemDetailView,
    PlaceBidView,
    AuctionItemCreateView,
    AuctionItemUpdateView,
    AuctionItemDeleteView,
)

urlpatterns = [
    path('api/auction-items/', AuctionItemListView.as_view(), name='auction_item_list'),
    path('api/auction-items/<int:id>/', AuctionItemDetailView.as_view(), name='auction_item_detail'),
    path('api/bids/', PlaceBidView.as_view(), name='place_bid'),
    path('api/auction-items/create/', AuctionItemCreateView.as_view(), name='auction_item_create'),
    path('api/auction-items/<int:id>/edit/', AuctionItemUpdateView.as_view(), name='auction_item_update'),
    path('api/auction-items/<int:id>/delete/', AuctionItemDeleteView.as_view(), name='auction_item_delete'),
]
