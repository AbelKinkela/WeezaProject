# Generated by Django 2.1.2 on 2019-05-12 11:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workermodel',
            old_name='buildingNumber',
            new_name='building_number',
        ),
        migrations.RenameField(
            model_name='workermodel',
            old_name='companyName',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='workermodel',
            old_name='fullName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='workermodel',
            old_name='nationalIDNumber',
            new_name='national_ID_number',
        ),
        migrations.AddField(
            model_name='workermodel',
            name='bank_account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='bank_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='emergency_contact_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='emergency_contact_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='emergency_contact_relationship',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='municipality',
            field=models.CharField(choices=[('CACUACO', 'Cacuaco'), ('KILAMBA', 'Kilamba-Kiaxi'), ('RANGEL', 'Rangel'), ('SAMBIZANGA', 'Sambizanga'), ('CAZENGA', 'Cazenga'), ('MAYANGA', 'Samba'), ('LUANDA', 'Luanda'), ('BELAS', 'Belas'), ('TALATONA', 'Talatona')], default='CACUACO', max_length=22),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='neighbourhood',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='province',
            field=models.CharField(choices=[('LUANDA', 'Luanda')], default='LUANDA', max_length=22),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='workdays',
            field=models.CharField(choices=[(0, 'Domingo'), (1, 'Segunda-Feira'), (2, 'Terça-Feira'), (3, 'Quarta-Feira'), (4, 'Quinta-Feira'), (5, 'Sexta-Feira'), (6, 'Sábado')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='years_of_experience',
            field=models.CharField(choices=[('one_years_experience', '1 ano ou menos'), ('two_years_experience', '2 anos'), ('three_years_experience', '3 anos'), ('four_years_experience', '4 anos'), ('5_years_experience', '5 anos ou mais')], default='one_years_experience', max_length=40),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '923 673 311'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='workermodel',
            name='service',
            field=models.CharField(choices=[('electronic_repair', 'Reparação de electrónicos'), ('home_cleaning', 'Limpeza de Casa'), ('electrician', 'Electricista'), ('plumbing', 'Canalização'), ('cold_and_air_conditioning', 'Frio e Climatização'), ('mechanic', 'Mecânico'), ('car_wash', 'Lavagem de Carro'), ('lock_smith', 'Serralheiro')], default='electronic_repair', max_length=100),
        ),
    ]