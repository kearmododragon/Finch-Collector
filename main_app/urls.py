
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path("about", views.about, name='about'),
  path("n64_index", views.allgames, name = 'n64_index')
]
