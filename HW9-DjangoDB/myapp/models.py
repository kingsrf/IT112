
from django.db import models

class Game(models.Model):
    # (Django automatically gives an auto-incrementing `id` field.)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.platform})"
