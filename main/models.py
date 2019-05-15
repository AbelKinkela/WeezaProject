from django.db import models
from accs.models import CustomerModel, WorkerModel


class TaskModel(models.Model):
    customer_name = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    # date the user submitted/created the form
    created_date = models.DateField(auto_now_add=True)
    # time the user submitted/created the form
    created_time = models.DateTimeField(auto_now_add=True)

    # date the task has to be done
    todo_date = models.DateField(auto_now=True)
    # time the task has to be done
    todo_time = models.DateTimeField()

    # the reported time that the task was completed
    completed_time = models.DateTimeField()

    # name of the company/individual the task was assigned to
    owner_name = models.ForeignKey(WorkerModel, on_delete=models.CASCADE)


class HouseCleaningTask(TaskModel):

    EXTRA_WORK_CHOICES = (
        ("CABINET", 'Inside Cabinet'),
        ("FRIDGE", 'Inside Fridge'),
        ("OVEN", 'Inside Oven'),
        ("WASHING", 'Laundry & Washing'),
        ("DOORS", 'Windows & Doors'),
    )
    extra_work = models.CharField(
        max_length=12,
        choices=EXTRA_WORK_CHOICES,
    )
    numberOfRooms = models.IntegerField()
    # duration = models.DateTimeField()  this should be run by a method
    detergent = models.BooleanField(default=True)


class PlumbingTask(TaskModel):
    PLUMBING_AREA_CHOICES = (
        ("KITCHEN", 'Kitchen Sink'),
        ("BATH", 'Bathroom Pipes'),
        ("TOILET", 'Toilet Pipes'),
        ("SAWAGE", 'Sewage Pipes ')
    )

    PLUMBING_FIX_CHOICES = (
        ("MAINTANCE", 'Maintanance'),
        ("INSTALATION", 'Installation'),
    )
    plumbingOption = models.CharField(
        max_length=12,
        choices=PLUMBING_FIX_CHOICES,
    )
    plumbingArea = models.CharField(
        max_length=12,
        choices=PLUMBING_AREA_CHOICES,
    )


class ElectricityTask(TaskModel):
    ELECTRIC_AREA_CHOICES = (
        ("BULB", 'Bulb Change'),
        ("SOCKET", 'Socket'),
        ("SWITCH", 'Switch'),
        ("EXTENSION", 'Extension'),
        ("SHOCK", 'Shock')
    )

    ELECTRIC_FIX_CHOICES = (
        ("MAINTANCE", 'Maintanance'),
        ("INSTALATION", 'Installation'),
    )
    electricOption = models.CharField(
        max_length=12,
        choices=ELECTRIC_FIX_CHOICES,
    )
    electricArea = models.CharField(
        max_length=12,
        choices=ELECTRIC_AREA_CHOICES,
    )
