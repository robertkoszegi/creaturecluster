from django.forms import ModelForm
from .models import Feeding, Creature

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class CreatureForm(ModelForm):
  class Meta:
    model = Creature
    fields = ['name', 'species', 'description', 'diet']