from django import forms
from .models import Marquee, MultipleChoiceQuestion, Choice

class MarqueeForm(forms.ModelForm):
    class Meta:
        model = Marquee
        fields = ['text', 'date', 'time']

class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ['question_text', 'course']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'is_correct']