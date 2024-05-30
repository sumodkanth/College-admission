# Generated by Django 5.0.2 on 2024-05-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUI', '0074_hostelroom_gender_alter_hostelroom_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelroom',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
    ]
