from django import forms

class Userform(forms.Form):
    fname = forms.CharField(label='First Name', max_length=16)
    lname = forms.CharField(label='Last Name', max_length=16)
    email = forms.EmailField()
