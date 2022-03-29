

from django import forms
from WebApp.models import Web_Model,Finance_Model
from WebApp.models import Remainder_Model

# create Model form
class Web_Modelform(forms.ModelForm):
    class Meta:
        model=Web_Model
        fields='__all__'
class Fin_Modelform(forms.ModelForm):
    class Meta:
        model=Finance_Model
        fields='__all__'
    
        
class Remainder_Modelform(forms.ModelForm):
    class Meta:
        model=Remainder_Model
        fields='__all__'


