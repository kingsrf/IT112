

from django.shortcuts import render, get_object_or_404
from .models import Game

def game_list_view(request):
    # Renders a template showing all Game objects, each linking to its detail page.
    games = Game.objects.all().order_by("id")
    return render(request, "myapp/game_list.html", {"games": games})

def game_detail_view(request, pk):
    # Renders a template showing details for the Game with primary key=pk.
    game = get_object_or_404(Game, pk=pk)
    return render(request, "myapp/game_detail.html", {"game": game})
