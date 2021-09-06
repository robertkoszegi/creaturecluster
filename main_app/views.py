from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Creature, Snack # imports the class from the models file
from .forms import FeedingForm, CreatureForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



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
    fields = ['name', 'species', 'description', 'diet']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreatureUpdate(LoginRequiredMixin, UpdateView):
    model = Creature
    fields = ['species', 'description', 'diet']


class CreatureDelete(LoginRequiredMixin, DeleteView):
    model = Creature
    success_url = '/creatures/'


# - Function based views - 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def creatures_index(request):
    # creatures = Creature.objects.filter(user=request.user).order_by('name') # query the imported model for rendering
    # alternative:
    creatures = request.user.creature_set.all()
    return render(request, 'creatures/index.html', {'creatures': creatures})

@login_required
def creatures_detail(request, creature_id):
    creature = Creature.objects.get(id=creature_id)
    # get snack that match the creature's diet
    matching_snacks = Snack.objects.filter(snacktype=creature.diet)
    snacks_remaining = matching_snacks.exclude(id__in=creature.snacks.values_list('id'))
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'creatures/detail.html', {
        # include the creature and feeding_form in the context
        'creature': creature, 
        'feeding_form': feeding_form,
        'snacks': snacks_remaining,
    })

@login_required
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

class SnackList(LoginRequiredMixin, ListView):
    model = Snack

class SnackDetail(LoginRequiredMixin, DetailView):
    model = Snack

class SnackCreate(LoginRequiredMixin, CreateView):
    model = Snack
    fields = '__all__'

class SnackUpdate(LoginRequiredMixin, UpdateView):
    model = Snack
    fields = ['name', 'snacktype']

class SnackDelete(LoginRequiredMixin, DeleteView):
    model = Snack
    success_url = '/snacks/'

def assoc_snack(request, creature_id, snack_id):
  Creature.objects.get(id=creature_id).snacks.add(snack_id)
  return redirect('detail', creature_id=creature_id)

def unassoc_snack(request, creature_id, snack_id):
  Creature.objects.get(id=creature_id).snacks.remove(snack_id)
  return redirect('detail', creature_id=creature_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        #Creates 'user' form object with data enered
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # add user to DB
            login(request, user) # log user in after signing up
            return redirect('index') # show index with record belonging to user
        else:error_message = 'Invalid sign up - try again'
    # Bad POST of GET request: show empy form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)