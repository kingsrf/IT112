
from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "genre", "platform", "release_year")
    search_fields = ("title", "genre", "platform")
    list_filter = ("platform", "release_year")