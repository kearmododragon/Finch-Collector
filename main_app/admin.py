# Register your models here.
from django.contrib import admin
# import your models here
from .models import Game, levels

# Register your models here
admin.site.register(Game)
admin.site.register(levels)