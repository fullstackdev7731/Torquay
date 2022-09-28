from django import forms
from .models import Visitor

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'
        exclude = ['user']