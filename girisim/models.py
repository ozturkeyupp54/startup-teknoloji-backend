from django.db import models
from django.core.validators import MaxLengthValidator
from user.models import User
from investor.models import IndustryCategory, IndustrySubcategory

class Girisim(models.Model):

    TURKISH_CITIES = [
        ('ADANA', 'ADANA'),
        ('ADIYAMAN', 'ADIYAMAN'),
        ('AFYONKARAHİSAR', 'AFYONKARAHİSAR'),
        ('AGRI', 'AGRI'),
        ('AMASYA', 'AMASYA'),
        ('ANKARA', 'ANKARA'),
        ('ANTALYA', 'ANTALYA'),
        ('ARTVIN', 'ARTVIN'),
        ('AYDIN', 'AYDIN'),
        ('BALIKESIR', 'BALIKESIR'),
        ('BILECIK', 'BILECIK'),
        ('BINGOL', 'BINGOL'),
        ('BITLIS', 'BITLIS'),
        ('BOLU', 'BOLU'),
        ('BURDUR', 'BURDUR'),
        ('BURSA', 'BURSA'),
        ('CANAKKALE', 'CANAKKALE'),
        ('CANKIRI', 'CANKIRI'),
        ('CORUM', 'CORUM'),
        ('DENIZLI', 'DENIZLI'),
        ('DIYARBAKIR', 'DIYARBAKIR'),
        ('EDIRNE', 'EDIRNE'),
        ('ELAZIG', 'ELAZIG'),
        ('ERZINCAN', 'ERZINCAN'),
        ('ERZURUM', 'ERZURUM'),
        ('ESKISEHIR', 'ESKISEHIR'),
        ('GAZIANTEP', 'GAZIANTEP'),
        ('GİRESUN', 'GİRESUN'),
        ('GUMUSHANE', 'GUMUSHANE'),
        ('HAKKARI', 'HAKKARI'),
        ('HATAY', 'HATAY'),
        ('ISPARTA', 'ISPARTA'),
        ('MERSIN', 'MERSIN'),
        ('ISTANBUL', 'ISTANBUL'),
        ('IZMIR', 'IZMIR'),
        ('KARS', 'KARS'),
        ('KASTAMONU', 'KASTAMONU'),
        ('KAYSERI', 'KAYSERI'),
        ('KIRKLARELI', 'KIRKLARELI'),
        ('KIRSEHIR', 'KIRSEHIR'),
        ('KOCAELI', 'KOCAELI'),
        ('KONYA', 'KONYA'),
        ('KUTAHYA', 'KUTAHYA'),
        ('MALATYA', 'MALATYA'),
        ('MANISA', 'MANISA'),
        ('KAHRAMANMARAS', 'KAHRAMANMARAS'),
        ('MARDIN', 'MARDIN'),
        ('MUGLA', 'MUGLA'),
        ('MUS', 'MUS'),
        ('NEVSEHIR', 'NEVSEHIR'),
        ('NIGDE', 'NIGDE'),
        ('ORDU', 'ORDU'),
        ('RIZE', 'RIZE'),
        ('SAKARYA', 'SAKARYA'),
        ('SAMSUN', 'SAMSUN'),
        ('SIIRT', 'SIIRT'),
        ('SINOP', 'SINOP'),
        ('SIVAS', 'SIVAS'),
        ('TEKIRDAG', 'TEKIRDAG'),
        ('TOKAT', 'TOKAT'),
        ('TRABZON', 'TRABZON'),
        ('TUNCELI', 'TUNCELI'),
        ('SANLIURFA', 'SANLIURFA'),
        ('USAK', 'USAK'),
        ('VAN', 'VAN'),
        ('YOZGAT', 'YOZGAT'),
        ('ZONGULDAK', 'ZONGULDAK'),
        ('AKSARAY', 'AKSARAY'),
        ('BAYBURT', 'BAYBURT'),
        ('KARAMAN', 'KARAMAN'),
        ('KIRIKKALE', 'KIRIKKALE'),
        ('BATMAN', 'BATMAN'),
        ('SIRNAK', 'SIRNAK'),
        ('BARTIN', 'BARTIN'),
        ('ARDAHAN', 'ARDAHAN'),
        ('IGDIR', 'IGDIR'),
        ('YALOVA', 'YALOVA'),
        ('KARABUK', 'KARABUK'),
        ('KILIS', 'KILIS'),
        ('OSMANIYE', 'OSMANIYE'),
        ('DUZCE', 'DUZCE'),
    ]

    CALISAN_SAYISI = [
      ('1-3', '1-3'),
      ('4-10', '4-10'),
      ('11-20', '11-20'),
      ('21-50', '21-50'),
      ('51-100', '51-100'),
      ('100+', '100+'),
      ]

    MENTOR_KEYS = [
    ('B2B', 'B2B'),
    ('B2C', 'B2C'),
    ('Basın', 'Basın'),
    ('Big Data', 'Big Data'),
    ('C2C', 'C2C'),
    ('Dağıtım', 'Dağıtım'),
    ('Denetim', 'Denetim'),
    ('Devlet İle İlişkiler', 'Devlet İle İlişkiler'),
    ('Donanım', 'Donanım'),
    ('Dış Ticaret', 'Dış Ticaret'),
    ('Dijital Pazarlama', 'Dijital Pazarlama'),
    ('E-Ticaret', 'E-Ticaret'),
    ('Fikir Doğrulama', 'Fikir Doğrulama'),
    ('Fiyatlandırma', 'Fiyatlandırma'),
    ('Fon Bulma', 'Fon Bulma'),
    ('Growth Hacking', 'Growth Hacking'),
    ('Gümrük', 'Gümrük'),
    ('Halkla İlişkiler', 'Halkla İlişkiler'),
    ('Hibe ve Destekler', 'Hibe ve Destekler'),
    ('Hukuk', 'Hukuk'),
    ('IoT', 'IoT'),
    ('IT', 'IT'),
    ('İnovasyon', 'İnovasyon'),
    ('İnsan Kaynakları', 'İnsan Kaynakları'),
    ('İçerik Pazarlama', 'İçerik Pazarlama'),
    ('İş Geliştirme', 'İş Geliştirme'),
    ('İş Modeli', 'İş Modeli'),
    ('İş Yönetimi', 'İş Yönetimi'),
    ('Kalite Yönetimi', 'Kalite Yönetimi'),
    ('Kitlesel Fonlama', 'Kitlesel Fonlama'),
    ('Liderlik', 'Liderlik'),
    ('Marka', 'Marka'),
    ('Muhasebe', 'Muhasebe'),
    ('Müşteri İlişkileri', 'Müşteri İlişkileri'),
    ('Patent', 'Patent'),
    ('Pazar Araştırması', 'Pazar Araştırması'),
    ]

    
    DEPARTMAN = [
        ("Mühendislik / Engineering", "Mühendislik / Engineering"),
        ("Yönetim / Management", "Yönetim / Management"),
        ("Ürün / Product", "Ürün / Product"),
        ("Finans / Finance", "Finans / Finance"),
        ("İnsan Kaynakları / Human Resources", "İnsan Kaynakları / Human Resources"),
        ("Bilgi Teknolojisi / Information Technology", "Bilgi Teknolojisi / Information Technology"),
        ("Hukuk / Legal", "Hukuk / Legal"),
        ("Pazarlama / Marketing", "Pazarlama / Marketing"),
        ("Tıp ve Bilim / Medical & Science", "Tıp ve Bilim / Medical & Science"),
        ("Operasyonel / Operations", "Operasyonel / Operations"),
        ("Profesyonel Hizmetler / Pro Services", "Profesyonel Hizmetler / Pro Services"),
        ("Satış / Sales", "Satış / Sales"),
        ("Destek / Support", "Destek / Support"),
    ]
    
    POZISYON = [
    ("Asistan / Assistant", "Asistan / Assistant"),
    ("Ortak / Partner", "Ortak / Partner"),
    ("Direktör, Operasyonlar / Director, Operations", "Direktör, Operasyonlar / Director, Operations"),
    ("Kıdemli Direktör / Senior Director", "Kıdemli Direktör / Senior Director"),
    ("Profesör / Professor", "Profesör / Professor"),
    ("Danışman / Consultant", "Danışman / Consultant"),
    ("Koordinatör / Coordinator", "Koordinatör / Coordinator"),
    ("Kıdemli Başkan Yardımcısı / Senior Vice President", "Kıdemli Başkan Yardımcısı / Senior Vice President"),
    ("Genel Müdür / General Manager", "Genel Müdür / General Manager"),
    ("Sahibi / Owner", "Sahibi / Owner"),
    ("Program Yöneticisi / Program Manager", "Program Yöneticisi / Program Manager"),
    ("CEO / CEO", "CEO / CEO"),
    ("Yönetici, Operasyonlar / Manager, Operations", "Yönetici, Operasyonlar / Manager, Operations"),
    ("Hesap Yöneticisi / Account Manager", "Hesap Yöneticisi / Account Manager"),
    ("Yönetici, Satış / Manager, Sales", "Yönetici, Satış / Manager, Sales"),
    ("Mühendis / Engineer", "Mühendis / Engineer"),
    ("Başkan / President", "Başkan / President"),
    ("Süpervizör / Supervisor", "Süpervizör / Supervisor"),
    ("Proje Yöneticisi / Project Manager", "Proje Yöneticisi / Project Manager"),
    ("Yönetmen / Director", "Yönetmen / Director"),
    ("Üst Düzey Yönetici / Executive", "Üst Düzey Yönetici / Executive"),
    ("Başkan Yardımcısı / Vice President", "Başkan Yardımcısı / Vice President"),
    ("Yönetici / Manager", "Yönetici / Manager"),
    ("Analist / Analyst", "Analist / Analyst"),
]




    class Meta:
        db_table = 'girisim'
        verbose_name = 'Girişim'
        verbose_name_plural = 'Girişimler'
        ordering = ['-pk']


    girisimci = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    girisimci_bilgileri_yayinlansin_mi = models.BooleanField(default=False, null=True, blank=True)
    girisim_adi = models.CharField(max_length=254, unique=True) #Girişim Adı
    girisim_ozeti = models.TextField(blank=True, null=True,validators=[MaxLengthValidator(limit_value=1000)])
    girisimin_is_modeli = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(limit_value=1000)])
    girisimin_pazar_ve_rekabet_durumu = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(limit_value=1000)])
    girisim_ile_ilgili_dokumanlarin_linki= models.URLField(blank=True, null=True)
    girisim_logo = models.ImageField(upload_to='girisim_logo/', default='', blank=True, null=True)
    girisim_kurulus_tarihi = models.DateField(blank=True, null=True)
    girisim_social_media_facebook = models.URLField(blank=True, null=True)
    girisim_social_media_linkedin = models.URLField(blank=True, null=True)
    girisim_social_media_youtube = models.URLField(blank=True, null=True)
    girisim_social_media_instagram = models.URLField(blank=True, null=True)
    girisim_social_media_twitter_x = models.URLField(blank=True, null=True)
    girisim_location_city = models.CharField(max_length=20,choices=TURKISH_CITIES, default = 'ISTANBUL')
    girisimin_calisan_sayisi = models.CharField(max_length=10, choices=CALISAN_SAYISI)
    sirketlestiniz_mi = models.BooleanField(default=False, null=True, blank=True) #Şirketleştiniz mi?
    sirket_logosu = models.ImageField(upload_to='company_logo/', default='', blank=True, null=True)
    sirketin_websitesi_varsa = models.URLField(blank=True, null=True)
    sirket_slogani = models.CharField(max_length=255, blank=True, null=True, unique=True)
    sirketin_kurulus_tarihi = models.DateField(blank=True, null=True)
    yatirim_alindi_mi = models.BooleanField(default=False, null=True, blank=True)
    alinan_yatirim_miktari = models.PositiveBigIntegerField(blank=True, null=True)
    sirketlesme_tamamlandi_mi = models.BooleanField(default=False, null=True, blank=True)
    fatura_kesiliyor_mu =  models.BooleanField(default=False, null=True, blank=True)
    calisma_durumu = models.BooleanField(default=False, null=True, blank=True)
    company_purchasing_merging = models.BooleanField(default=False, null=True, blank=True)
    sirket_borsaya_acildi_mi = models.BooleanField(default=False, null=True, blank=True) #Firma borsaya açıldı mı?
    

    girisimin_bulundugu_sektor = models.ForeignKey(IndustryCategory, blank=True, null=True, on_delete=models.SET_NULL) #Girişim Ana Sektörünüz Nedir?
    girisimin_bulundugu_altsektor = models.ForeignKey(IndustrySubcategory, blank=True, null=True, on_delete=models.SET_NULL) #Girişim Ana Sektörünüz Nedir?
    girisim_mentorluk_ihtiyac_alanlari = models.CharField(max_length=40,choices=MENTOR_KEYS) #Mentorluk İhtiyaç Alanlarınız Nelerdir?
    
    girisim_ozeti= models.TextField(blank=True, null=True, validators=[MaxLengthValidator(limit_value=1000)]) #Girişim Özeti
    yatirimci_sunumu = models.FileField(upload_to='yatirimci_sunumu/', default='', blank=True, null=True)
    finansman_kullanildi_mi = models.BooleanField(default=False, null=True, blank=True)
    son_finansman_tarihi = models.DateField(blank=True, null=True)
    son_finansman_turu = models.CharField(max_length=254, blank=True, null=True)
    son_finansman_miktari = models.PositiveBigIntegerField(blank=True, null=True)
    toplam_finansman_miktari = models.PositiveBigIntegerField(blank=True, null=True)    
    
    ekip_arkadasi_adi= models.CharField(max_length=80, blank=True, null=True)
    ekip_arkadasi_soyadi= models.CharField(max_length=80, blank=True, null=True)
    ekip_arkadasi_email= models.CharField(max_length=80, blank=True, null=True)
    ekip_arkadasi_telefonu= models.CharField(max_length=13, blank=True, null=True)
    ekip_arkadasi_linkedin = models.URLField(blank=True, null=True)
    ekip_arkadasi_departmani = models.CharField(max_length=80,choices=DEPARTMAN, blank=True, null=True)
    ekip_arkadasi_calistigi_pozisyon= models.CharField(max_length=80, choices=POZISYON, blank=True, null=True)   
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f" {self.girisimci} - {self.girisim_adi} "
       

class GirisimHaberleri(models.Model):  
    class Meta:
        db_table = 'girisimHaberleri'
        verbose_name = 'GirisimHaberi'
        verbose_name_plural = 'GirisimHaberleri'
        ordering = ['-pk']
        
    girisimci = models.ForeignKey(User, on_delete=models.CASCADE)
    haber_tarihi = models.DateField()
    haber_basligi = models.CharField(max_length=255)
    haber_linki = models.URLField()
    haberin_ilgili_oldugu_girisim = models.ForeignKey(Girisim, on_delete=models.CASCADE)
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f"{self.haber_basligi}. {self.haberin_ilgili_oldugu_girisim}"      
      

class GirisimGelismelerHedefler(models.Model):  
    class Meta:
        db_table = 'girisimGelismelerHedefler'
        verbose_name = 'girisimGelismelerHedefler'
        verbose_name_plural = 'girisimGelismelerHedefleri'
        ordering = ['-pk']
        
    girisimci = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    gelisme_veya_hedef_tarihi = models.DateField(blank=True, null=True)
    gelisme_veya_hedef_aciklamasi = models.CharField(max_length=240)
    target_to_girisim = models.ForeignKey(Girisim, on_delete=models.CASCADE, blank=True, null=True)
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f"{self.gelisme_veya_hedef_aciklamasi}. {self.target_to_girisim}" 
    
    
class GirisiminYatirimTurlari(models.Model):  
    class Meta:
        db_table = 'girisiminYatirimTurlari'
        verbose_name = 'GirisimYatirimi'
        verbose_name_plural = 'GirisimYatirimlari'
        ordering = ['-pk']
    
    ROUND_TIPI=[
        ('Pre-Seed','Pre-Seed'),
        ('Seed','Seed'),
        ('Seri A','Sei A'),
    ]
    
    YATIRIM_TURU_AKTIF_ESKI=[
        ('Aktif Yatırım Turu','Aktif Yatırım Turu'),
        ('Eski Yatırım Turu','Eski Yatırım Turu'),
    ]
    
    girisimci = models.ForeignKey(User, on_delete=models.CASCADE)
    round_tipi = models.CharField(max_length=10,choices=ROUND_TIPI, default = 'Pre-Seed')
    round_tutari = models.PositiveBigIntegerField()
    sirketin_degeri = models.PositiveBigIntegerField()
    yatirim_turu_baslangic_tarihi= models.DateField()
    yatirim_turu_bitis_tarihi= models.DateField()
    yatirimin_ilgili_oldugu_girisim = models.ForeignKey(Girisim, on_delete=models.CASCADE)    
    yatirim_turu_aktif_veya_eski = models.CharField(max_length=20,choices=YATIRIM_TURU_AKTIF_ESKI, default = 'Aktif Yatırım Turu')
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f"{self.round_tipi}. {self.yatirim_turu_aktif_veya_eski}"      
      