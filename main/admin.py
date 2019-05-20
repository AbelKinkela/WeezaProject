from django.contrib import admin
from .models import ElectricityTask, HouseCleaningTask, PlumbingTask

# Register your models here.
admin.site.register(ElectricityTask)
admin.site.register(HouseCleaningTask)
admin.site.register(PlumbingTask)
