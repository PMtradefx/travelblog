from django.shortcuts import render
from .models import Projecto

def home(request):
    projects = Projecto.objects.all()
    return render(request,'home.html', {'projects':projects})
# Create your views here.
