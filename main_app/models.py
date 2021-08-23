from django.db import models

# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    diet = models.CharField(max_length=100)

    def __str__(self):
        return self.name