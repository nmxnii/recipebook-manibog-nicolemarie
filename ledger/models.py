from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Ingredient(models.Model): 
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('Ingredient_detail', args=[str(self.name)])
class Recipe(models.Model): 
    name = models.CharField(max_length=100) 
    author = models.CharField(max_length=100) 
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.name)])
class RecipeIngredient(models.Model): 
    quantity = models.CharField(max_length=100)
    ingredientF = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipeF = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients' )



     

