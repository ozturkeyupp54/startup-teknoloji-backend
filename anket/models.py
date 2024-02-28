from django.db import models
from django.core.validators import MaxLengthValidator
from user.models import User

class Anket(models.Model):

    class Meta:
        db_table = 'anket'
        verbose_name = 'Anket'
        verbose_name_plural = 'Anketler'
        ordering = ['-pk']
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    anket_baslik = models.CharField(max_length=255)
    aciklama = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(limit_value=800)])
    anket_baslik_resmi = models.ImageField(upload_to='anket_baslik_resmi/', default='', blank=True, null=True)
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.anket_baslik
        

    def get_questions(self):
        return self.soru_set.all()

class Soru(models.Model):
    
    QUESTION_TYPE_CHOICES = [
        ('MULTIPLE_CHOICE', 'Çoktan Seçmeli'),
        ('OPEN_ENDED_SHORT_ANSWER', 'Açık Uçlu-Kısa Cevap'),
        ('OPEN_ENDED_PARAGRAPH', 'Açık Uçlu-Paragraf'),
        ('YES_NO', 'Evet/Hayır'),
        ('DATE', 'Tarih'),
        ('TIME', 'Zaman'),
    ]
    
    class Meta:
        db_table = 'anket_sorulari'
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'
        ordering = ['-pk']
        
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    anket = models.ForeignKey(Anket, related_name='sorular', on_delete=models.CASCADE)
    icerik = models.CharField(max_length=255)
    question_type = models.CharField(max_length=40, choices=QUESTION_TYPE_CHOICES, default='OPEN_ENDED')

    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.icerik
    
    def get_answers(self):
        return self.cevap_set.all()
    

    
class Secenek(models.Model):
    class Meta:
        db_table = 'secenekler'
        verbose_name = 'Secenek'
        verbose_name_plural = 'Secenekler'
        ordering = ['-pk']
        
    soru = models.ForeignKey(Soru, on_delete=models.CASCADE, related_name='secenekler')
    icerik = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.icerik
    
    def get_soru_type(self):
        return self.soru.question_type



class Cevap(models.Model):

    class Meta:
        db_table = 'anket_cevapları'
        verbose_name = 'Cevap'
        verbose_name_plural = 'Cevaplar'
        ordering = ['-pk']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    soru = models.ForeignKey(Soru, on_delete=models.CASCADE)
    kisa_cevap = models.CharField(max_length=255, null=True, blank=True)
    uzun_cevap = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(limit_value=1000)])
    secenek = models.ForeignKey(Secenek, on_delete=models.CASCADE, null=True, blank=True)
    evet_hayir = models.BooleanField(default=True, null=True, blank=True)
    tarih = models.DateField(null=True, blank=True)
    zaman = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Soru: {self.soru.icerik}, Cevap: {self.secenek}, Cevap: {self.evet_hayir}, Cevap: {self.tarih}, Cevap: {self.zaman}"
    
    def get_sorunun_secenekleri(self):
        return Secenek.objects.filter(soru=self.soru)
    
class Sonuc(models.Model):
    
    class Meta:
        db_table = 'anket_sonucu'
        verbose_name = 'Sonuc'
        verbose_name_plural = 'Sonuclar'
        ordering = ['-pk']
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anket = models.ForeignKey(Anket, on_delete=models.CASCADE)
    cevap= models.ForeignKey(Cevap,on_delete=models.CASCADE)
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    
    def __str__(self):
        return str(self.pk)
    

    
# from django.db import models

# MC = 'MC'
# CN = 'CN'
# TX = 'TX'

# CATEGORY = (
#     (MC, 'Multichoice'),
#     (CN, 'Choose N'),
#     (TX, 'Text'),
# )

# VALYK = '1'
# VALKA = '2'
# VALKO = '3'
# VALNE = '4'
# VALVI = '5'

# MULTICHOICE = (
#     (VALYK, 'Least'),
#     (VALKA, 'Less than average'),
#     (VALKO, 'Average'),
#     (VALNE, 'More than average'),
#     (VALVI, 'Most'),
# )

# class Questionnaire(models.Model):
#     questionnaire_name = models.CharField(max_length=100,
#                                           verbose_name="Questionnaire",
#                                           null=False,
#                                           default=None,
#                                           blank=False)
#     def __str__(self):
#         return self.questionnaire_name

# class Question(models.Model):
#     questionnaire = models.ManyToManyField(Questionnaire)
#     question_text = models.CharField(max_length=200,
#                                      verbose_name="Questionnaire name",
#                                      null=True,
#                                      default=None,
#                                      blank=True)
#     question_category = models.CharField(max_length=2,
#                                          verbose_name="Question category",
#                                          null=False,
#                                          choices=CATEGORY,
#                                          default=None,
#                                          blank=False)
#     def __str__(self):
#         return self.question_text

# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text_answer = models.CharField(max_length=255, blank=True, null=True)

# class MultiChoiceAnswer(Answer):
#     answer = models.IntegerField(choices=MULTICHOICE)
#     def __str__(self):
#         return self.answer
