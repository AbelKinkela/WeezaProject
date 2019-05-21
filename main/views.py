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


def cold_and_air_conditioning(request):
    form_class = ElectricityTaskForm()
    return render(request, 'main/cold_and_air_conditioning.html', {'form': form_class})


def car_washing(request):
    form_class = ElectricityTaskForm()
    return render(request, 'main/car_washing.html', {'form': form_class})


def mechanic(request):
    form_class = ElectricityTaskForm()
    return render(request, 'main/mechanic.html', {'form': form_class})


def lock_smith(request):
    form_class = ElectricityTaskForm()
    return render(request, 'main/lock_smith.html', {'form': form_class})


def electronic_device_repair(request):
    form_class = ElectricityTaskForm()
    return render(request, 'main/electronic_device_repair.html', {'form': form_class})
