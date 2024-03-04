from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient
class RecipeInLine(admin.TabularInline):
    model = Recipe
class IngredientInLine(admin.TabularInline):
    model = Ingredient
class RecipeInInLine(admin.TabularInline):
    model = RecipeIngredient
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInInLine, ] 
    list_display = ['name'] 

class IngredientAdmin(admin.ModelAdmin): 
    model = Ingredient

    list_display = ['name']
# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
