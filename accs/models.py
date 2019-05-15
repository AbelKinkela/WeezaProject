from django.db import models
from django.core.validators import RegexValidator


class WorkerModel(models.Model):
    # Personal details
    name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    phone = models.IntegerField()
    email = models.EmailField()
    national_ID_number = models.CharField(
        max_length=130, blank=True, null=True)

    company_name = models.CharField(max_length=130, blank=True, null=True)
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

    SERVICE_CHOICES = (
        ("electronic_repair", 'Reparação de electrónicos'),
        ("home_cleaning", 'Limpeza de Casa'),
        ("electrician", 'Electricista'),
        ("plumbing", 'Canalização'),
        ("cold_and_air_conditioning", 'Frio e Climatização'),
        ("mechanic", 'Mecânico'),
        ("car_wash", 'Lavagem de Carro'),
        ("lock_smith", 'Serralheiro'),
    )
    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES,
        default="electronic_repair",
    )

    YEARS_OF_EXPERIENCE_CHOICES = (
        ('one_years_experience', '1 ano ou menos'),
        ('two_years_experience', '2 anos'),
        ('three_years_experience', '3 anos'),
        ('four_years_experience', '4 anos'),
        ('5_years_experience', '5 anos ou mais'),
    )

    years_of_experience = models.CharField(
        max_length=40,
        choices=YEARS_OF_EXPERIENCE_CHOICES,
        default="one_years_experience",
    )

    WORKDAYS_CHOICES = (
        (0, 'Domingo'),
        (1, 'Segunda-Feira'),
        (2, 'Terça-Feira'),
        (3, 'Quarta-Feira'),
        (4, 'Quinta-Feira'),
        (5, 'Sexta-Feira'),
        (6, 'Sábado'),

    )

    workdays = models.CharField(
        max_length=1,
        choices=WORKDAYS_CHOICES,
        null=True,
        default=1,
    )

    # Banking Information (not applicable in the form right now)
    BANKNAME_CHOICES = (
        ("bank_BAI", 'BANCO ANGOLANO DE INVESTIMENTOS, S.A. BAI'),
        ("bank_YETU", 'BANCO YETU, S.A. YETU'),
        ("bank_BMF", 'BANCO BAI MICRO FINANÇAS, S.A. BMF'),
        ("bank_BIC", 'BANCO BIC, S.A. BIC'),
        ("bank_BCGA", 'BANCO CAIXA GERAL ANGOLA, S.A. BCGA'),
        ("bank_BCA", 'BANCO COMERCIAL ANGOLANO, S.A. BCA'),
        ("bank_BCH", 'BANCO COMERCIAL DO HUAMBO, S.A. BCH'),
        ("bank_BCI", 'BANCO DE COMÉRCIO E INDÚSTRIA, S.A. BCI'),
        ("bank_BDA", 'BANCO DE DESENVOLVIMENTO DE ANGOLA, S.A. BDA'),
        ("bank_BFA", 'BANCO DE FOMENTO ANGOLA, S.A. BFA'),
        ("bank_BIR", 'BANCO DE INVESTIMENTO RURAL, S.A. BIR'),
        ("bank_BNI", 'BANCO DE NEGÓCIOS INTERNACIONAL, S.A. BNI'),
        ("bank_BPC", 'BANCO DE POUPANÇA E CRÉDITO, S.A. BPC'),
        ("bank_BE", 'BANCO ECONÓMICO, S.A. BE'),
        ("bank_KEVE", 'BANCO KEVE, S.A. KEVE'),
        ("bank_BKI", 'BANCO KWANZA INVESTIMENTO, S.A. BKI'),
        ("bank_BPG", 'BANCO PRESTÍGIO, S.A. BPG'),
        ("bank_ATL", 'BANCO MILLENNIUM ATLÂNTICO, S.A. ATL'),
        ("bank_BSOL", 'BANCO SOL, S.A. BSOL'),
        ("bank_BVB", 'BANCO VALOR, S.A. BVB'),
        ("bank_VTB", 'BANCO VTB ÁFRICA, S.A. VTB'),
        ("bank_FNB", 'FINIBANCO ANGOLA, S.A. FNB'),
        ("bank_SBA", 'STANDARD BANK DE ANGOLA, S.A. SBA'),
        ("bank_SCBA", 'STANDARD CHARTERED BANK DE ANGOLA, S.A. SCBA'),
        ("bank_BCS", 'BCS – BANCO DE CRÉDITO DO SUL, S.A. BCS'),
        ("bank_BOCLB", 'BANCO DA CHINA LIMITADA – SUCURSAL EM LUANDA BOCLB'),
    )

    bank_name = models.CharField(
        max_length=100, choices=BANKNAME_CHOICES, null=True)
    bank_account_number = models.CharField(
        max_length=100, blank=True, null=True)

    # Emergency details
    emergency_contact_name = models.CharField(
        max_length=100, blank=True, null=True)
    emergency_contact_number = models.IntegerField(null=True)
    emergency_contact_relationship = models.CharField(
        max_length=100, blank=True, null=True)


class CustomerModel(models.Model):
    fullName = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '923 673 311'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
