from django import forms
from bigcow.models import CowInput


class AddTextInput(forms.Form):
    cow_input = forms.CharField()
