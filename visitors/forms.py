from django import forms
from .models import (Reservation, Comment)
from datetime import date

class ReservationForm(forms.ModelForm):

    ROOM_SIZES = ((2,'Small'),(3,'Small +'),(4,'Medium'),(5,'Large'),(6,'Suite'))

    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out']
        labels = {
            'check_in' : 'Check in',
            'check_out' : 'Check out'
        }
        widgets = {
            'check_in' : forms.SelectDateWidget(),
            'check_out' : forms.SelectDateWidget()
        }

    room_size = forms.ChoiceField(choices=ROOM_SIZES)

    def clean(self):
        date_in = self.cleaned_data['check_in']
        date_out = self.cleaned_data['check_out']

        if date_in < date.today():
            raise forms.ValidationError("Invalid Pass Date!")

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'rating')
    