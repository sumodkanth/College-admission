# Generated by Django 4.0.5 on 2023-10-18 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FacultyUI', '0004_remove_facultydb_contact_remove_facultydb_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultydb',
            name='Type',
        ),
    ]
