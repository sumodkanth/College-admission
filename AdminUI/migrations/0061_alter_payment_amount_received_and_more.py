# Generated by Django 5.0.2 on 2024-04-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUI', '0060_alter_admissiondb_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount_received',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cvv',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expiration_date',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
