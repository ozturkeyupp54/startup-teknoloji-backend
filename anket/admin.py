from django import forms
from django.contrib import admin
from anket.models import Anket, Soru, Cevap, Sonuc, Secenek


class SecenekInline(admin.TabularInline):
    model = Secenek
    list_display = ('icerik', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['icerik', 'soru__icerik']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'soru':
            # Seçili sorunun tipini al
            selected_question_type = Soru.objects.get(pk=request.resolver_match.kwargs['object_id']).question_type
            # Soru tipine göre seçenekleri filtrele
            kwargs['queryset'] = Secenek.objects.filter(soru=request.resolver_match.kwargs['object_id'], soru__question_type=selected_question_type)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CevapInline(admin.TabularInline):
    model = Cevap
    list_display = ('soru', 'cevap', 'user', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['soru', 'cevap', 'user']

class SoruInline(admin.TabularInline):  # Burayı admin.StackedInline olarak değiştirin
    model = Soru
    inlines = [SecenekInline, CevapInline]
    list_display = ('anket', 'icerik', 'user', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['anket', 'icerik', 'user']

class AnketAdmin(admin.ModelAdmin):
    inlines = [SoruInline]
    list_display = ('anket_baslik', 'aciklama', 'user', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['baslik', 'aciklama', 'user']

class SonucAdmin(admin.ModelAdmin):
    list_display = ('anket', 'user', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['anket', 'user']
    
class SecenekAdmin(admin.ModelAdmin):
    list_display = ('icerik', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['icerik', 'user']
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'soru':
            # Soru modelinde sadece MULTIPLE_CHOICE tipindeki soruları seçenek olarak göster
            kwargs['queryset'] = Soru.objects.filter(question_type='MULTIPLE_CHOICE')

        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class CevapAdminForm(forms.ModelForm):
    class Meta:
        model = Cevap
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # İlgili sorunun ID'sini al
        soru_id = self.initial.get('soru')
        if soru_id:
            # İlgili sorunun tipini al
            soru_tipi = Soru.objects.get(pk=soru_id).question_type
            # Soru tipine göre sadece ilgili alanı göster
            if soru_tipi == 'MULTIPLE_CHOICE':
                self.fields['secenek'].widget = forms.widgets.AdminTextInputWidget()
                
            elif soru_tipi == 'OPEN_ENDED_SHORT_ANSWER':
                self.fields['kisa_cevap'].widget = forms.widgets.AdminTextInputWidget()

            # Diğer durumlar için aynı şekilde devam edebilirsiniz
            return self


class CevapAdmin(admin.ModelAdmin):
    form = CevapAdminForm
    list_display = ('user', 'soru', 'secenek', 'kisa_cevap', 'uzun_cevap', 'evet_hayir', 'tarih', 'zaman', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted', 'soru__question_type')
    search_fields = ['user__username', 'soru__icerik', 'secenek__icerik']

admin.site.register(Cevap, CevapAdmin)
admin.site.register(Anket, AnketAdmin)
# SoruInline ve CevapInline'ı burada kaydetmeyin
admin.site.register(Soru)
admin.site.register(Sonuc, SonucAdmin)
admin.site.register(Secenek, SecenekAdmin)

# from django.contrib import admin
# from .models import Questionnaire, Question, Answer, MultiChoiceAnswer

# # Register your models here.

# @admin.register(Questionnaire)
# class QuestionnaireAdmin(admin.ModelAdmin):
#     list_display = ['questionnaire_name']
#     ordering = ['-id']

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ['question_text', 'question_category', 'get_questionnaires']
#     ordering = ['-id']

#     def get_questionnaires(self, obj):
#         return ", ".join([q.questionnaire_name for q in obj.questionnaire.all()])

# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     pass

# @admin.register(MultiChoiceAnswer)
# class MultiChoiceAnswerAdmin(admin.ModelAdmin):
#     list_display = ['answer']
#     ordering = ['-id']


