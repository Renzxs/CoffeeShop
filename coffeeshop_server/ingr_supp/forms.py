from django import forms
from .models import Ingr

class IngrForm(forms.ModelForm):
    class Meta:
        model = Ingr
        fields = ['ingr_name', 'ingr_quant', 'ingr_desc', 'ingr_catg', 'ingr_cost', 'ingr_suppNo', 'ingr_exp','ingr_date', 'ingr_act']

class IngrFormUp(forms.ModelForm):
    class Meta:
        model = Ingr
        fields = ['ingr_name', 'ingr_quant', 'ingr_act']