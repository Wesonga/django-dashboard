from django import forms
from .models import ProjectMetric


class ProjectMetricForm(forms.ModelForm):

  class Meta:
    model = ProjectMetric
    fields = ['title', 'value', 'badge_text']
    widgets = {
        'title': forms.TextInput(
            attrs={'class': 'form-input', 'placeholder': 'e.g. LATENCY'}
        ),
        'value': forms.TextInput(
            attrs={'class': 'form-input', 'placeholder': 'e.g. 14ms'}
        ),
        'badge_text': forms.TextInput(
            attrs={'class': 'form-input', 'placeholder': 'e.g. Optimal'}
        ),
    }
