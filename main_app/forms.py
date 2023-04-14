from django.forms import ModelForm
from .models import levels

class LevelsForm(ModelForm):
  class Meta:
    model = levels
    fields = ['number', 'name']
