# Generated by Django 5.0.2 on 2024-04-15 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUI', '0055_busbooking_student_id_alter_busbooking_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='bus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminUI.busbooking'),
        ),
    ]
