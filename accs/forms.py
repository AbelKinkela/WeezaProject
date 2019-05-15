
from .models import WorkerModel, CustomerModel
from django import forms

#


class WorkerForm(forms.ModelForm):
    class Meta:
        model = WorkerModel
        fields = '__all__'
        widgets = {'workdays': forms.CheckboxSelectMultiple}
        labels = {
            "name": "Nome",
            "last_name": "Sobrenome",
            "phone": "Número de celular",
            "email": "Email",
            "national_ID_number": "Possuidor do Bilhete de Identidade Nº",
            "company_name": "Nome da Empresa",
            "building_number": "Edifício Nº",
            "street": "Morra na rua",
            "neighbourhood": "Bairro",
            "municipality": "Município",
            "province": "Provincia",
            "service": "Serviço",
            "years_of_experience": "Anos de experiência",
            "workdays": "Dias de Trabalho",
            "bank_name": "Nome do Banco",
            "bank_account_number": "Número da conta",
            "emergency_contact_name": "Nome do contacto de emergência",
            "emergency_contact_number": "Número de emergência",
            "emergency_contact_relationship": "Relação",
        }
