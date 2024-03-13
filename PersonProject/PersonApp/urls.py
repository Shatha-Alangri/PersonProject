from django.urls import path
from .views import add, show_people

urlpatterns = [
    path('add/', add, name='add'),
    path('', show_people, name='show_people'),
]