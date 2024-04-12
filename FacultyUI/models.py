from django.db import models

from AdminUI.models import DepartmentDB,FacultyEnrollmentDB


# Create your models here.


class FacultyDB(models.Model):
    FacultyID = models.ForeignKey(FacultyEnrollmentDB, on_delete=models.CASCADE)
    AltContact = models.CharField(max_length=20, null=True, blank=True)
    DoB = models.DateField(null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Bank = models.CharField(max_length=200, null=True, blank=True)
    Acc_Number = models.IntegerField(null=True, blank=True)
    IFSC = models.CharField(max_length=20, null=True, blank=True)
    Photo = models.ImageField(upload_to="Faculty", null=True, blank=True)
