from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.


def home(request):
    return render(request, 'html/index.html')
