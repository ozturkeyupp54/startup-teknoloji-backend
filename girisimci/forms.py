from django import forms
from girisimci.models import Girisimci

class GirisimciForm(forms.ModelForm):
    class Meta:
        model = Girisimci
        fields = '__all__'
