from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings  # Assuming the User model is the default Django user mode
from AdminUI.models import JobsDB
class SelectionStatus(models.Model):
    STATUS_CHOICES = [
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(JobsDB, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.job.title} - {self.status}"


