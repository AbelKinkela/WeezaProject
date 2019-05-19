from django.shortcuts import render
from .models import WorkerModel, CustomerModel
from .forms import WorkerForm
from django.views.generic import CreateView
# Create your views here.


# class WorkerModelCreateView(CreateView):
#     template_name = 'html/worker_sign_up.html'
#     form_class = WorkerForm
#     model = WorkerModel


def WorkerModelCreateView(request):
    form_class = WorkerForm()
    return render(request, 'accs/worker_sign_up.html', {'form': form_class})
