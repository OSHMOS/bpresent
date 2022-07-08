from .models import Card, Name
from django import forms

class CardForm(forms.ModelForm):
  class Meta:
    model = Card
    fields = ['title',]


class NameForm(forms.ModelForm):
  class Meta:
    model = Name
    exclude = ['card', 'dt_attend', 'dt_late', 'dt_absent',]