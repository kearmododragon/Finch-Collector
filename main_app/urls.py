
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path("about", views.about, name='about'),
  path("N64_games", views.allfinches, name = 'N64_games')
]
