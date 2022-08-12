from django.urls import path

from recipes.views import home, contact

urlpatterns = [
    path('', home),
    path('contact/', contact),
]
