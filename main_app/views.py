from django.shortcuts import render
n64 = [
  {"name": "Mario Kart 64", "genre": "Racing", "franchise": "Mario"},
  {"name": "Pokemon Stadium", "genre": "stratergy", "franchise": "Pokemon"},
  ]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def allfinches(request):
  return render(request, 'n64_index.html', {'n64': n64})