from .models import HouseCleaningTask, PlumbingTask, ElectricityTask
from django import forms

#

translated_labels = {
    "customer_name": "Nome",
    "email": "Email",
    "phone_number": "Número de telemóvel",
    "description": "Mais details sobre a tarefa",
    "price": "Preço",
    "todo_date": "Data",
    "todo_time": "Hora",
    "building_number": "Casa Nº",
    "street": "Morra na rua",
    "neighbourhood": "Bairro",
    "municipality": "Município",
    "province": "Provincia",
    "extra_work": "A incluir",
    "numberOfRooms": "Número de Quartos",
    "detergent": "Trazer detergente e outros productos de limpeza",
}

common_fields = ["customer_name", "phone_number", "email", "description",
                 "price", "todo_date", "todo_time", "building_number",
                 "street", "neighbourhood", "municipality", "province"]


class HouseCleaningTaskForm(forms.ModelForm):
    class Meta:
        model = HouseCleaningTask
        fields = common_fields + ["extra_work", "numberOfRooms", "detergent"]

        labels = translated_labels


class PlumbingTaskForm(forms.ModelForm):
    class Meta:
        model = PlumbingTask
        fields = common_fields + ["plumbingOption", "plumbingArea"]

        labels = translated_labels


class ElectricityTaskForm(forms.ModelForm):
    class Meta:
        model = ElectricityTask
        fields = common_fields

        labels = translated_labels
