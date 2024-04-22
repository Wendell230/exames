from django import forms
from .models import TiposExames

class TiposExamesForm(forms.ModelForm):
    class Meta:
        model = TiposExames
        fields = '__all__'  
