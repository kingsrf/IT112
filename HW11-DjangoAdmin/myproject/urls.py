
from django.contrib import admin
from django.urls import path
from myapp.views import game_list_view, game_detail_view 
from myapp.views import api_all_games, api_get_game, api_create_game  # new import for HW10

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", game_list_view, name="home"),
    path("games/", game_list_view, name="game_list"),    
    path("games/<int:pk>/", game_detail_view, name="game_detail"), 
    
    # New API endpoints for HW10
    path("api/games/", api_all_games, name="api_all_games"),  # new
    path("api/game/", api_get_game, name="api_get_game"),  # new
    path("api/games/create/", api_create_game, name="api_create_game"),  # new
]
