from django.shortcuts import render, get_object_or_404
import random
from .models import Mineral


def mineral_detail(request, name):
    """shows details of a specific mineral"""
    mineral = get_object_or_404(Mineral, name=name)
    return render(request, 'detail.html', {'mineral': mineral})


def random_mineral(request):
    """selects a random mineral and renders the detail page for that mineral"""
    full_list = Mineral.objects.all()
    mineral = random.choice(full_list)
    return render(request, 'detail.html', {'mineral': mineral})


def index(request):
    """list of all minerals"""
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})
