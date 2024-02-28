from django import forms
from django.forms.widgets import DateInput
from girisim.models import Girisim, GirisimHaberleri, GirisimGelismelerHedefler, GirisiminYatirimTurlari
from investor.models import IndustryCategory, IndustrySubcategory


from django import forms

class GirisimForm(forms.ModelForm):
    class Meta:
        model = Girisim
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GirisimForm, self).__init__(*args, **kwargs)
        self.fields['girisimin_bulundugu_sektor'].queryset = IndustryCategory.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        selected_category = cleaned_data.get('girisimin_bulundugu_sektor')
        if selected_category:
            # Filter subcategories based on the selected category
            subcategories = IndustrySubcategory.objects.filter(category=selected_category)
            self.fields['girisimin_bulundugu_altsektor'].queryset = subcategories

        return cleaned_data


class GirisimHaberleriForm(forms.ModelForm):
    class Meta:
        model = GirisimHaberleri
        fields = ['haber_tarihi', 'haber_basligi', 'haber_linki', 'haberin_ilgili_oldugu_girisim']
        widgets = {
            'haber_tarihi': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(GirisimHaberleriForm, self).__init__(*args, **kwargs)
        self.fields['haber_tarihi'].widget.attrs['placeholder'] = 'Haberin Tarihini Girin'
        self.fields['haber_basligi'].widget.attrs['placeholder'] = 'Haberin Başlığını Girin'
        self.fields['haber_linki'].widget.attrs['placeholder'] = 'Haberin Linkini Girin'

        
class GirisimGelismelerHedeflerForm(forms.ModelForm):
    class Meta:
        model = GirisimGelismelerHedefler
        fields = ['gelisme_veya_hedef_tarihi', 'gelisme_veya_hedef_aciklamasi']

    def __init__(self, *args, **kwargs):
        super(GirisimGelismelerHedeflerForm, self).__init__(*args, **kwargs)
        # Customize the form if needed, for example, adding placeholders or additional widgets
        self.fields['gelisme_veya_hedef_tarihi'].widget.attrs['placeholder'] = 'Enter Development or Target Date'
        self.fields['gelisme_veya_hedef_aciklamasi'].widget.attrs['placeholder'] = 'Enter Development or Target Description'


class GirisiminYatirimTurlariForm(forms.ModelForm):
    class Meta:
        model = GirisiminYatirimTurlari
        fields = ['round_tipi', 'round_tutari', 'sirketin_degeri', 'yatirim_turu_baslangic_tarihi', 'yatirim_turu_bitis_tarihi', 'yatirimin_ilgili_oldugu_girisim', 'yatirim_turu_aktif_veya_eski']

    def __init__(self, *args, **kwargs):
        super(GirisiminYatirimTurlariForm, self).__init__(*args, **kwargs)

        self.fields['round_tutari'].widget.attrs['placeholder'] = 'Round Turarı Değerini Girin'

