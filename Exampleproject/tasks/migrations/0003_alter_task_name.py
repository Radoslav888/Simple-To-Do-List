# Generated by Django 4.2.7 on 2023-12-18 19:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Task'),
        ),
    ]
