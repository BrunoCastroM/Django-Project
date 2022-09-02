from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
from django.http import Http404


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    # Put the specific path to avoid conflict. Ex: "recipes/home.html"
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes, })
    # The django search automatically the name path of "templates", because it's configurate in "settings.py" file, but you can configure it


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404('Not found 🥲')


    return render(request, 'recipes/pages/category.html', context={'recipes': recipes, 'title': f'{recipes.first().category.name} - Category | '})


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': make_recipe(), 'is_detail_page': True})
