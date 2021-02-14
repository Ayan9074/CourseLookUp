from django import forms
from .models import Course

class NameForm(forms.Form):
    searchby = forms.CharField()