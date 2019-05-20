from django.shortcuts import render
from .models import WorkerModel, CustomerModel
from .forms import WorkerForm
from django.views.generic import CreateView
from django.shortcuts import redirect
# Create your views here.


# class WorkerModelCreateView(CreateView):
#     template_name = 'html/worker_sign_up.html'
#     form_class = WorkerForm
#     model = WorkerModel


def WorkerModelCreateView(request):
    form_class = WorkerForm()

    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = WorkerForm()

    return render(request, 'accs/worker_sign_up.html', {'form': form_class})
