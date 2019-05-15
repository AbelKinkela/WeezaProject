from .models import WorkerModel, CustomerModel
from django import forms


class WorkerForm(forms.ModelForm):
    class Meta:
        model = WorkerModel
        fields = '__all__'
        widgets = {'': forms.CheckboxSelectMultiple}
        labels = {

        }
