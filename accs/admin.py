from django.contrib import admin
from .models import CustomerModel, WorkerModel
# Register your models here.


class WorkerModelAdmin(admin.ModelAdmin):

    list_display = ["name", "email",
                    "company_name", "phone_number", "service"]

    class Meta:
        model = WorkerModel


admin.site.register(WorkerModel, WorkerModelAdmin)
admin.site.register(CustomerModel)
