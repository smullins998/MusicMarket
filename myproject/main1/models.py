from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artist_images/')
    biography = models.TextField()
    stock_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def current_price(self):
        # Implement your logic to get the current price
        # This is just a placeholder, replace with your actual implementation
        return self.stock_price

class Position(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    shares = models.PositiveIntegerField()
    average_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s position in {self.artist.name}"

    @property
    def total_value(self):
        return self.shares * self.artist.current_price()

    @property
    def gain_loss(self):
        return self.total_value - (self.shares * self.average_price)

    @property
    def gain_loss_percentage(self):
        if self.average_price > 0:
            return (self.gain_loss / (self.shares * self.average_price)) * 100
        return 0

class Order(models.Model):
    BUY = 'BUY'
    SELL = 'SELL'
    ORDER_TYPES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
    num_shares = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_type} order for {self.num_shares} shares of {self.artist.name} by {self.user.username}"

    @property
    def total_value(self):
        return self.num_shares * self.price
