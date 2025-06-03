
from django.shortcuts import render, get_object_or_404
from .models import Game
import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


def game_list_view(request):
    # Renders a template showing all Game objects, each linking to its detail page.
    games = Game.objects.all().order_by("id")
    return render(request, "myapp/game_list.html", {"games": games})

def game_detail_view(request, pk):
    # Renders a template showing details for the Game with primary key=pk.
    game = get_object_or_404(Game, pk=pk)
    return render(request, "myapp/game_detail.html", {"game": game})

# HW10: Django REST API views

@require_GET
def api_all_games(request):
    # Returns a JSON list of all Game records.
    games = Game.objects.all().order_by("id")
    data = [
        {
            "id": g.id,
            "title": g.title,
            "genre": g.genre,
            "platform": g.platform,
            "release_year": g.release_year,
        }
        for g in games
    ]
    return JsonResponse(data, safe=False)  # safe=False allows returning a list

@require_GET
def api_get_game(request):
    # Returns JSON for a single Game record by its ID.
    game_id = request.GET.get("id")
    if not game_id:
        return JsonResponse(
            {"error": "Missing query parameter 'id'."},
            status=200,
            json_dumps_params={"indent": 2},
        )

    try:
        game = Game.objects.get(pk=int(game_id))
        data = {
            "id": game.id,
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "release_year": game.release_year,
        }
        return JsonResponse(data, status=200, json_dumps_params={"indent": 2})
    except (ValueError, Game.DoesNotExist):
        return JsonResponse(
            {"error": f"No game found with id={game_id}."},
            status=200,
            json_dumps_params={"indent": 2},
        )

@require_POST
def api_create_game(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
        title = payload["title"]
        genre = payload["genre"]
        platform = payload["platform"]
        release_year = int(payload["release_year"])
    except (KeyError, ValueError, json.JSONDecodeError) as e:
        return JsonResponse(
            {"error": "Invalid JSON or missing fields in request body.", "details": str(e)},
            status=200,
            json_dumps_params={"indent": 2},
        )

    # Creates and saves the new Game
    try:
        new_game = Game.objects.create(
            title=title, genre=genre, platform=platform, release_year=release_year
        )
        return JsonResponse(
            {
                "success": f"Game '{new_game.title}' (id={new_game.id}) created successfully."
            },
            status=200,
            json_dumps_params={"indent": 2},
        )
    except Exception as e:
        return JsonResponse(
            {"error": "Failed to create new game.", "details": str(e)},
            status=200,
            json_dumps_params={"indent": 2},
        )