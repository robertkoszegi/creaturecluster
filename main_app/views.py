from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Creature  # imports the class from the models file

# In place of real databse
# class Creature:
#     def __init__(self, name, species, description, diet):
#         self.name = name
#         self.species = species
#         self.description = description
#         self.diet = diet
    
# creatures = [
#     Creature('Muffin', 'tarantula', 'friendly', 'animals'),
#     Creature('Spot', 'salamander', 'slimey', 'animals'),
#     Creature('Speedy', 'sloth', 'slow', 'plants'),
# ]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Creature Cluster</h1>')

def about(request):
    return render(request, 'about.html')

def creatures_index(request):
    creatures = Creature.objects.all().order_by('id') # query the imported model for rendering
    return render(request, 'creatures/index.html', {'creatures': creatures})

def creatures_detail(request, creature_id):
    creature = Creature.objects.get(id=creature_id)
    return render(request, 'creatures/detail.html', {'creature': creature})