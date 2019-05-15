# Generated by Django 2.1.2 on 2019-05-12 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accs', '0002_auto_20190512_1539'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ElectricityTaskModel',
            new_name='ElectricityTask',
        ),
        migrations.RenameModel(
            old_name='Plumbing',
            new_name='PlumbingTask',
        ),
        migrations.RenameField(
            model_name='taskmodel',
            old_name='taskTime',
            new_name='completed_time',
        ),
        migrations.RenameField(
            model_name='taskmodel',
            old_name='customerName',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='taskmodel',
            old_name='taskDescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='taskmodel',
            old_name='taskName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='taskmodel',
            old_name='ownerName',
            new_name='owner_name',
        ),
        migrations.RenameField(
            model_name='taskmodel',
            old_name='taskPrice',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='taskmodel',
            old_name='taskDate',
            new_name='todo_date',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2019, 5, 12, 11, 38, 13, 924403, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 5, 12, 11, 38, 24, 207155, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='todo_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 12, 11, 39, 34, 959756, tzinfo=utc)),
            preserve_default=False,
        ),
    ]