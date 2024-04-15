from django import forms
from .models import SelectionStatus
from django.contrib.auth.forms import UserCreationForm
from AdminUI.models import Booking

class SelectionStatusForm(forms.ModelForm):
    class Meta:
        model = SelectionStatus
        fields = ['job', 'status']
        widgets = {
            'status': forms.RadioSelect,
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date']