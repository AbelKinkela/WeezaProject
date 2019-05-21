from django.db import models
from accs.models import CustomerModel, WorkerModel
from django.core.validators import RegexValidator


class TaskModel(models.Model):
    # customer_name = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200, blank=False, null=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="O número deve seguir o formato: '923673311'")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    # date the user submitted/created the form
    created_date = models.DateField(auto_now_add=True)
    # time the user submitted/created the form
    created_time = models.DateTimeField(auto_now_add=True)

    # date the task has to be done
    todo_date = models.DateField(null=True)
    # time the task has to be done
    todo_time = models.DateTimeField(null=True)

    # the reported time that the task was completed
    completed_time = models.DateTimeField(null=True)

    # name of the company/individual the task was assigned to
    owner_name = models.ForeignKey(WorkerModel, on_delete=models.CASCADE)

    building_number = models.CharField(max_length=130, blank=True, null=True)
    # Address
    # It is still not possible to identify all household by Nº in Angola. Applicable to established companies only
    street = models.CharField(max_length=200, blank=True, null=True)
    neighbourhood = models.CharField(max_length=200, blank=True, null=True)

    MUNICIPALITY_CHOICES = (
        ("CACUACO", 'Cacuaco'),
        ("KILAMBA", 'Kilamba-Kiaxi'),
        ("RANGEL", 'Rangel'),
        ("SAMBIZANGA", 'Sambizanga'),
        ("CAZENGA", 'Cazenga'),
        ("MAYANGA", 'Samba'),
        ("LUANDA", 'Luanda'),
        ("BELAS", 'Belas'),
        ("TALATONA", 'Talatona'),
    )

    municipality = models.CharField(
        max_length=22,
        choices=MUNICIPALITY_CHOICES,
    )

    PROVINCE_CHOICES = (
        ("LUANDA", 'Luanda'),
    )
    province = models.CharField(
        max_length=22,
        choices=PROVINCE_CHOICES,
        default="LUANDA",
    )


class HouseCleaningTask(TaskModel):

    EXTRA_WORK_CHOICES = (
        ("CABINET", 'Dentro do Armário'),
        ("FRIDGE", 'Dentro da arca'),
        ("OVEN", 'Dentro do fogão'),
        ("WASHING", 'Lavar a loiça'),
        ("DOORS", 'Limpar janelas(de vidro, etc)'),
    )
    extra_work = models.CharField(
        max_length=30,
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


class CarWashTask(TaskModel):
    CAR_SIZE_CHOICES = (
        ("SMALL", 'Pequeno'),
        ("MEDIUM", 'Médio'),
        ("BIG", 'Grande'),
    )
    carSize = models.CharField(
        max_length=12,
        choices=CAR_SIZE_CHOICES,
    )


class ElectronicDeviceRepairTask(TaskModel):
    DEVICE_CHOICES = (
        ("PHONE", 'Telephone'),
        ("TV", 'Televisão'),
        ("DESKTOP", 'Computador de Mesa'),
        ("LAPTOP", 'Laptop'),
        ("RADIO", 'Rádio, Amplificador'),
        ("OTHER", 'Outro'),

    )
    deviceType = models.CharField(
        max_length=12,
        choices=DEVICE_CHOICES,
    )


class Mecanic(TaskModel):
    problemDescription = models.CharField(
        max_length=500, blank=True, null=True)


class LockSmithTask(TaskModel):
    whatTodo = models.CharField(
        max_length=500, blank=True, null=True)


class ElectricityTask(TaskModel):
    whatTodo = models.CharField(
        max_length=500, blank=True, null=True)
