from django.shortcuts import render


def home(request):
    # Put the specific path to avoid conflict. Ex: "recipes/home.html"
    return render(request, 'recipes/pages/home.html',)
    # The django search automatically the name path of "templates", because it's configurate in "settings.py" file, but you can configure it
