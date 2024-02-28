from django import forms
from alt_reklam_alani.models import FooterReklami
from datetime import date

class ReklamForm(forms.ModelForm):
    class Meta:
        model = FooterReklami
        fields = ['kampanya_basligi', 'kampanya_creator_adi','kampanya_creator_soyadi','sirket_adi', 'reklam_gosterim_yeri','kampanya_baslangic_tarihi',  'advertisement_alt_resmi', 'kampanyanin_websitesinin_linki', 'max_views_per_image']

    widgets = {
        
        'advertisement_alt_resmi': forms.FileInput(attrs={'accept': 'image/*'}),
        'kampanyanin_websitesinin_linki': forms.URLInput(attrs={'placeholder': 'Markanızın web adresini girin'}),
        'kampanya_creator_adi': forms.TextInput(attrs={'placeholder': 'Adınızı girin'}),
        'kampanya_creator_soyadi': forms.TextInput(attrs={'placeholder': 'Soyadınızı girin'}),
        'kampanya_baslangic_tarihi': forms.DateInput(attrs={'type': 'date'}),
        'reklam_gosterim_yeri': forms.Select(attrs={'class': 'form-select mt-2'}),
    }

    def clean_kampanya_baslangic_tarihi(self):
            kampanya_baslangic_tarihi = self.cleaned_data.get('kampanya_baslangic_tarihi')

            # Check if the selected date is in the past
            if kampanya_baslangic_tarihi and kampanya_baslangic_tarihi < date.today():
                raise ValidationError('Kampanya başlangıç tarihi geçmiş bir tarih olamaz.')

            return kampanya_baslangic_tarihi

    def clean_max_views_per_image(self):
        max_views_per_image = self.cleaned_data.get('max_views_per_image')
        if max_views_per_image is not None and max_views_per_image < 1:
            raise forms.ValidationError("Max views per image must be at least 1.")
        return max_views_per_image
