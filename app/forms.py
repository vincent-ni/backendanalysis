from django import forms

class NameBox(forms.Form):
    name = forms.CharField(widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': "Book Name"}))

class LongBox(forms.Form):
    longitude = forms.CharField(widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': "Longitude"}))

class LatBox(forms.Form):
    latitude = forms.CharField(widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': "Latitude"}))

class RadiusBox(forms.Form):
    radius = forms.CharField(widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': "Radius"}))
