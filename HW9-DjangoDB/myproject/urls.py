
from django.contrib import admin
from django.urls import path
from myapp.views import game_list_view, game_detail_view  # added detail, removed home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", game_list_view, name="home"),
    path("games/", game_list_view, name="game_list"),       # new
    path("games/<int:pk>/", game_detail_view, name="game_detail"),  #new
]
