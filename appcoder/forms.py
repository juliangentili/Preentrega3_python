from django import forms

class neumaticoFormulario(forms.Form):
    marca= forms.CharField(max_length=40)
    rodado= forms.IntegerField()

class tuercasFormulario(forms.Form):
    marca = forms.CharField(max_length=40) 
    precio = forms.IntegerField()
    