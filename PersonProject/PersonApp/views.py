from django.shortcuts import render
from .models import Person

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person.objects.create(username=username, password=password)

    return render(request, 'add.html')

def show_people(request):
    people = Person.objects.all()
    return render(request, 'show_people.html', {'people': people})
