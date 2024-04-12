from django.contrib import admin
from django.contrib import admin
from .models import SelectionStatus

@admin.register(SelectionStatus)
class SelectionStatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'status']