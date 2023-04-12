
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path("about", views.about, name='about'),
  path("n64_games", views.allfinches, name = 'n64_games')
]
