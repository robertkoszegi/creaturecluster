from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

SNACKTYPE = (
    ('animal', 'Animal'),
    ('plant', 'Plant'),
)

class Snack(models.Model):
  name = models.CharField(max_length=50)
  snacktype = models.CharField(
      max_length=20,
      choices=SNACKTYPE, 
      null=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('snacks_detail', kwargs={'pk': self.id})

# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    snacks = models.ManyToManyField(Snack)
    diet = models.CharField(
        max_length=20,
        choices=SNACKTYPE,
        null=True,
        default=SNACKTYPE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'creature_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    ) 
    # Create a creature_id FK
    creature = models.ForeignKey(Creature, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
