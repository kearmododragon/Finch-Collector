from django.shortcuts import render
from .models import Game
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
  return render(request, 'N64_games/details.html', { 'n64': game })
