from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(label='Enter your needs', max_length=100)
