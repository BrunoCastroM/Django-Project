from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    # Put the specific path to avoid conflict. Ex: "recipes/home.html"
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes, })
    # The django search automatically the name path of "templates", because it's configurate in "settings.py" file, but you can configure it


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes, })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': make_recipe(), 'is_detail_page': True})
