from django import forms

class TextBox(forms.Form):
    query = forms.CharField(widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': 'Location'}))
