# Generated by Django 5.0.2 on 2024-04-18 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUI', '0059_admissiondb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissiondb',
            name='DateOfBirth',
            field=models.CharField(max_length=10),
        ),
    ]
