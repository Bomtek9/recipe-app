from django.db import models
from django.shortcuts import reverse


# Create your models here.


class Recipe (models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(default=-1, help_text='in minutes')
    ingredients = models.CharField(max_length=350, default='')
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_image.svg')

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

    # calculate difficulty of recipe using cooking time and number of ingredients
    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 30 and len(ingredients) < 7:
            difficulty = 'Easy'
        elif self.cooking_time < 30 and len(ingredients) >= 7:
            difficulty = 'Medium'
        elif self.cooking_time >= 30 and len(ingredients) < 7:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 30 and len(ingredients) >= 7:
            difficulty = 'Hard'
        return difficulty

    def __str__(self):
        return str(self.name)