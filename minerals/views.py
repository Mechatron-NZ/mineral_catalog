from django.shortcuts import render, get_object_or_404
from .models import Mineral


def detail(request, name):
    mineral = get_object_or_404(Mineral, name=name)
    return render(request, 'minerals/detail.html', {'mineral': mineral})
