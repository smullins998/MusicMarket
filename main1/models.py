from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

    def __str__(self):
        return self.name