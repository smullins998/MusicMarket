from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artist_images/')
    biography = models.TextField()
    stock_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
