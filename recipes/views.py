from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    # Put the specific path to avoid conflict. Ex: "recipes/home.html"
    return render(request, 'recipes/pages/home.html', context={'recipes': [make_recipe() for _ in range(3)], })
    # The django search automatically the name path of "templates", because it's configurate in "settings.py" file, but you can configure it


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': make_recipe(), 'is_detail_page': True})
