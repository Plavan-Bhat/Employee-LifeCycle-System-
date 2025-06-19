from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        widgets = {
            'date_of_interview': forms.DateInput(attrs={'type': 'date'}),
        }
