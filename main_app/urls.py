
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path("about/", views.about, name='about'),
  path("n64_index/", views.n64_index, name = 'n64_index'),
  path('n64_index/<int:game_id>/', views.games_detail, name='detail'),
  path('n64_index/create/', views.GameCreate.as_view(), name="game-create"),
  path('n64_index/<int:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
  path('n64_index/<int:pk>/delete/', views.GameDelete.as_view(),  name='game-delete'),
]
