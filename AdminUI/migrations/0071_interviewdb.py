# Generated by Django 5.0.2 on 2024-05-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUI', '0070_alter_multiplechoicequestion_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('InterviewStatus', models.CharField(blank=True, choices=[('Passed', 'Passed'), ('Failed', 'Failed')], max_length=10, null=True)),
            ],
        ),
    ]
