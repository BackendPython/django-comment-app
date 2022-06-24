from dataclasses import fields
from django import forms
from .models import *


class Login(forms.ModelForm):
    class Meta:
        model = My
        fields = (
            'name',
            'comment',
        )

class User(forms.ModelForm):
    class Meta:
        model = Down
        fields = (
            'name',
            'height',
        )