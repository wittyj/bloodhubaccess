# Generated by Django 4.2.1 on 2023-05-28 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]