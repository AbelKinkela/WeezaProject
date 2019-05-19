from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.


def home(request):
    return render(request, 'main/index.html')


def worker_sign_up(request):
    return