from django import forms
from AppGym.models import Rutina

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'