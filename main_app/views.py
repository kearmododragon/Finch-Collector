from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import LevelsForm

# Define the home view


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def n64_index(request):
    n64 = Game.objects.all()
    return render(request, 'N64_games/index.html', {'n64': n64})


def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    print(game_id)
    levels_form = LevelsForm()
    return render(request, 'N64_games/details.html', {'n64': game, "levels_form": levels_form})


def add_levels(request, game_id):
    form = LevelsForm(request.POST)
    if form.is_valid():
        new_level = form.save(commit=False)
        new_level.game_id = game_id
        new_level.save()
    return redirect("detail", game_id=game_id)


class GameCreate(CreateView):
    model = Game
    fields = '__all__'


class GameUpdate(UpdateView):
    model = Game
    fields = ["genre", "franchise", "description"]


class GameDelete(DeleteView):
    model = Game
    success_url = "/n64_index"
