from django.db import models
from django.shortcuts import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from cloudinary.models import CloudinaryField

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(default=-1, help_text='in minutes')
    ingredients = models.CharField(max_length=350, default='')
    description = models.TextField()
    difficulty = models.CharField(max_length=20, blank=True)
    pic = models.ImageField(upload_to='recipes', default='no_picture.png')

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

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

    def image_tag(self):
        if self.pic:
            return mark_safe('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(self.pic.url))
        else:
            return mark_safe('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format('/media/no_picture.png'))


    image_tag.short_description = 'Image'
