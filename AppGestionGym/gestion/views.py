from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'gestion/index.html')

def groupe(request):
    groupe = Groupe.objects.all()
    context = {'list_tuple_groupe': groupe}
    return render(request, 'gestion/groupe.html', context)

def adherent(request):
    adherent = Adherent.objects.all()
    context = {'list_tuple_adherent': adherent}
    return render(request, 'gestion/adherent.html', context)

def encadrant(request):
    encadrant = Encadrant.objects.all()
    context = {'list_tuple_encadrant': encadrant}
    return render(request, 'gestion/encadrant.html', context)