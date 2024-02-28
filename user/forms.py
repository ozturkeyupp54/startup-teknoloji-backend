from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'kvkk', 'is_electronic_commerce']
        labels = {
            'first_name': 'Adınız *',
            'last_name': 'Soyadınız *',
            'email': 'E-posta Adresiniz *',
            'phone': 'Telefon',
            'kvkk': 'Gizlilik Politikası *',
            'is_electronic_commerce': 'Üyelik Sözleşmesi *'
        }

