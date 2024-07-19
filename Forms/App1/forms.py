from django import forms
class Emp(forms.Form):
    idno = forms.IntegerField()
    name = forms.CharField()
    sal = forms.DecimalField()