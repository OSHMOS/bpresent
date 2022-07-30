from .models import Card, Name, Bookmark
from django import forms

class CardForm(forms.ModelForm):
  class Meta:
    model = Card
    fields = ['title',]


class NameForm(forms.ModelForm):
  class Meta:
    model = Name
    fields = ['name',]


class BookmarkForm(forms.ModelForm):
  class Meta:
    model = Bookmark
    fields= ['title',]