from django import forms
from anket.models import Anket, Soru

class AnketForm(forms.ModelForm):
    class Meta:
        model = Anket
        fields = ['anket_baslik', 'aciklama', 'anket_baslik_resmi']  # Add or remove fields as needed

class SoruForm(forms.ModelForm):
    class Meta:
        model = Soru
        fields = ['text']  # Add or remove fields as needed


# class AnketOlusturForm(forms.Form):
#     baslik = forms.CharField(max_length=255, label='Anket Başlığı')
#     aciklama = forms.CharField(widget=forms.Textarea, label='Açıklama')

# class SoruEkleForm(forms.Form):
#     icerik = forms.CharField(max_length=255, label='Soru İçeriği')

# from django import forms
# from anket.models import Questionnaire, Question, MultiChoiceAnswer, MULTICHOICE

# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Questionnaire  # Corrected model
#         fields = ['questionnaire_name']  # Assuming these fields exist in Questionnaire

#         # widgets = {
#         #     'field1': forms.RadioSelect(choices=MULTICHOICE, attrs={'required': True}),
#         #     'field2': forms.HiddenInput(),
#         # }

#     def __init__(self, *args, question=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         if question:
#             # Dynamically adjust choices and field types based on question category
#             if question.question_category == 'MC':
#                 self.fields['questionnaire_name'].choices = question.multichoiceanswer_set.all().values_list('id', 'answer')
#             elif question.question_category == 'CN':
#                 pass
#             elif question.question_category == 'TX':
#                 self.fields['questionnaire_name'] = forms.CharField(widget=forms.Textarea)
#             else:
#                 raise ValueError("Form requires a 'question' argument")
