from django import forms
from .models import SelectionStatus
from django.contrib.auth.forms import UserCreationForm


class SelectionStatusForm(forms.ModelForm):
    class Meta:
        model = SelectionStatus
        fields = ['job', 'status']
        widgets = {
            'status': forms.RadioSelect,
        }

# class RegForm(UserCreationForm):
#     class Meta:
#         model=CustUser
#         fields=['username','email','first_name','last_name','password1','password2']
#     username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control","style":"border-radius: 0.75rem; "}))
#     email=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email","class":"form-control","style":"border-radius: 0.75rem; "}))
#     first_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","class":"form-control","style":"border-radius: 0.75rem; "}))
#     last_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name","class":"form-control","style":"border-radius: 0.75rem; "}))
#     password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control","style":"border-radius: 0.75rem; "}))
#     password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","class":"form-control","style":"border-radius: 0.75rem; "}))
#     def clean_password2(self):
#         password1=self.cleaned_data.get('password1')
#         password2=self.cleaned_data.get('password2')
#         if password1 and password2 and password1!=password2:
#             raise forms.ValidationError('Password Does Not Match')
        
#         min_length=8
#         if len(password2)<min_length:
#             raise forms.ValidationError(f"Password must be atlease {min_length} characters long")
#         return super().clean_password2()