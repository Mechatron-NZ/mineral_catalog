from django.shortcuts import render, get_object_or_404
from .models import Mineral


def mineral_detail(request, name):
    mineral = Mineral.objects.get(name=name)
    #mineral = get_object_or_404(Mineral, name=name)
    return render(request, 'detail.html', {'mineral': mineral})


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})
