from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Creature  # imports the class from the models file
from .forms import FeedingForm



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
# - Class based views -
class CreatureCreate(CreateView):
    model = Creature
    fields = '__all__'

class CreatureUpdate(UpdateView):
    model = Creature
    fields = ['species', 'description', 'diet']

class CreatureDelete(DeleteView):
    model = Creature
    success_url = '/creatures/'


# - Function based views - 
def home(request):
    return HttpResponse('<h1>Creature Cluster</h1>')

def about(request):
    return render(request, 'about.html')

def creatures_index(request):
    creatures = Creature.objects.all().order_by('id') # query the imported model for rendering
    return render(request, 'creatures/index.html', {'creatures': creatures})

def creatures_detail(request, creature_id):
    creature = Creature.objects.get(id=creature_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'creatures/detail.html', {
        # include the creature and feeding_form in the context
        'creature': creature, 'feeding_form': feeding_form
    })

def add_feeding(request, creature_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the creature_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.creature_id = creature_id
    new_feeding.save()
  return redirect('detail', creature_id=creature_id)