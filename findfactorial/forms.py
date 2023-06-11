from django import forms

class UserNumber(forms.Form):
    num = forms.IntegerField()
