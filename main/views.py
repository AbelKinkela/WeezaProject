from django.shortcuts import render
from django.views.generic import CreateView
from .forms import HouseCleaningTaskForm, PlumbingTaskForm, ElectricityTaskForm
# Create your views here.


def home(request):
    return render(request, 'main/index.html')


def houseCleaning(request):
    form_class = HouseCleaningTaskForm()
    return render(request, 'main/houseCleaning.html', {'form': form_class})


def plumbing(request):
    form_class = PlumbingTaskForm()
    return render(request, 'main/plumbing.html', {'form': form_class})


def electricity(request):
    form_class = ElectricityTaskForm()
    return render(request, 'main/electricity.html', {'form': form_class})
