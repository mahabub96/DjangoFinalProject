# Create your models here.
from django.db import models
from users.models import User  # Import User model
from categories.models import Category  # Import Category model

class AuctionItem(models.Model):
    title = models.CharField(max_length=200)  # Item title
    description = models.TextField()  # Item description
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)  # Starting price
    current_price = models.DecimalField(max_digits=10, decimal_places=2)  # Current price
    end_date = models.DateTimeField()  # Auction end date
    is_sold = models.BooleanField(default=False)  # Track if the item is sold ext
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Category (Foreign Key)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auction_items')  # Seller (Foreign Key)
    created_at = models.DateTimeField(auto_now_add=True)  # Date created

    def __str__(self):
        return self.title
