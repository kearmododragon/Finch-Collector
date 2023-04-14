from django.shortcuts import render
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
  Levels_Form = LevelsForm()
  return render(request, 'N64_games/details.html', { 'n64': game })


class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  fields = ["genre", "franchise", "description"]

class GameDelete(DeleteView):
    model = Game
    success_URL = "/N64_games"   
