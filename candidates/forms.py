from .models import Candidate
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('candidate_id', 'name','address_number', 'address', 'year', 'month', 'day', 'univ', 'department', 'course', 'enroll_date', 'graduate_date', 'carrer_vision')
