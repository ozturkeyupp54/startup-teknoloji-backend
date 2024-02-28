# Generated by Django 4.2.9 on 2024-02-11 09:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Girisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('girisimci_bilgileri_yayinlansin_mi', models.BooleanField(blank=True, default=False, null=True)),
                ('girisim_adi', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('girisimin_is_modeli', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=1000)])),
                ('girisimin_pazar_ve_rekabet_durumu', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=1000)])),
                ('girisim_ile_ilgili_dokumanlar', models.URLField(blank=True, null=True)),
                ('girisim_logo', models.ImageField(blank=True, default='', null=True, upload_to='girisim_logo/')),
                ('girisim_kurulus_tarihi', models.DateField(blank=True, null=True)),
                ('girisim_social_media_facebook', models.URLField(blank=True, null=True)),
                ('girisim_social_media_linkedin', models.URLField(blank=True, null=True)),
                ('girisim_social_media_youtube', models.URLField(blank=True, null=True)),
                ('girisim_social_media_instagram', models.URLField(blank=True, null=True)),
                ('girisim_social_media_twitter_x', models.URLField(blank=True, null=True)),
                ('girisim_location_city', models.CharField(choices=[('ADANA', 'ADANA'), ('ADIYAMAN', 'ADIYAMAN'), ('AFYONKARAHİSAR', 'AFYONKARAHİSAR'), ('AGRI', 'AGRI'), ('AMASYA', 'AMASYA'), ('ANKARA', 'ANKARA'), ('ANTALYA', 'ANTALYA'), ('ARTVIN', 'ARTVIN'), ('AYDIN', 'AYDIN'), ('BALIKESIR', 'BALIKESIR'), ('BILECIK', 'BILECIK'), ('BINGOL', 'BINGOL'), ('BITLIS', 'BITLIS'), ('BOLU', 'BOLU'), ('BURDUR', 'BURDUR'), ('BURSA', 'BURSA'), ('CANAKKALE', 'CANAKKALE'), ('CANKIRI', 'CANKIRI'), ('CORUM', 'CORUM'), ('DENIZLI', 'DENIZLI'), ('DIYARBAKIR', 'DIYARBAKIR'), ('EDIRNE', 'EDIRNE'), ('ELAZIG', 'ELAZIG'), ('ERZINCAN', 'ERZINCAN'), ('ERZURUM', 'ERZURUM'), ('ESKISEHIR', 'ESKISEHIR'), ('GAZIANTEP', 'GAZIANTEP'), ('GİRESUN', 'GİRESUN'), ('GUMUSHANE', 'GUMUSHANE'), ('HAKKARI', 'HAKKARI'), ('HATAY', 'HATAY'), ('ISPARTA', 'ISPARTA'), ('MERSIN', 'MERSIN'), ('ISTANBUL', 'ISTANBUL'), ('IZMIR', 'IZMIR'), ('KARS', 'KARS'), ('KASTAMONU', 'KASTAMONU'), ('KAYSERI', 'KAYSERI'), ('KIRKLARELI', 'KIRKLARELI'), ('KIRSEHIR', 'KIRSEHIR'), ('KOCAELI', 'KOCAELI'), ('KONYA', 'KONYA'), ('KUTAHYA', 'KUTAHYA'), ('MALATYA', 'MALATYA'), ('MANISA', 'MANISA'), ('KAHRAMANMARAS', 'KAHRAMANMARAS'), ('MARDIN', 'MARDIN'), ('MUGLA', 'MUGLA'), ('MUS', 'MUS'), ('NEVSEHIR', 'NEVSEHIR'), ('NIGDE', 'NIGDE'), ('ORDU', 'ORDU'), ('RIZE', 'RIZE'), ('SAKARYA', 'SAKARYA'), ('SAMSUN', 'SAMSUN'), ('SIIRT', 'SIIRT'), ('SINOP', 'SINOP'), ('SIVAS', 'SIVAS'), ('TEKIRDAG', 'TEKIRDAG'), ('TOKAT', 'TOKAT'), ('TRABZON', 'TRABZON'), ('TUNCELI', 'TUNCELI'), ('SANLIURFA', 'SANLIURFA'), ('USAK', 'USAK'), ('VAN', 'VAN'), ('YOZGAT', 'YOZGAT'), ('ZONGULDAK', 'ZONGULDAK'), ('AKSARAY', 'AKSARAY'), ('BAYBURT', 'BAYBURT'), ('KARAMAN', 'KARAMAN'), ('KIRIKKALE', 'KIRIKKALE'), ('BATMAN', 'BATMAN'), ('SIRNAK', 'SIRNAK'), ('BARTIN', 'BARTIN'), ('ARDAHAN', 'ARDAHAN'), ('IGDIR', 'IGDIR'), ('YALOVA', 'YALOVA'), ('KARABUK', 'KARABUK'), ('KILIS', 'KILIS'), ('OSMANIYE', 'OSMANIYE'), ('DUZCE', 'DUZCE')], default='ISTANBUL', max_length=20)),
                ('girisimin_calisan_sayisi', models.CharField(choices=[('1-3', '1-3'), ('4-10', '4-10'), ('11-20', '11-20'), ('21-50', '21-50'), ('51-100', '51-100'), ('100+', '100+')], max_length=10)),
                ('sirketlestiniz_mi', models.BooleanField(blank=True, default=False, null=True)),
                ('sirket_logosu', models.ImageField(blank=True, default='', null=True, upload_to='company_logo/')),
                ('sirketin_websitesi', models.URLField(blank=True, null=True)),
                ('sirket_slogani', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('sirketin_kurulus_tarihi', models.DateField(blank=True, null=True)),
                ('sirketin_sosyal_medya_hesabi', models.URLField(blank=True, null=True)),
                ('yatirim_alindi_mi', models.BooleanField(blank=True, default=False, null=True)),
                ('alinan_yatirim_miktari', models.PositiveBigIntegerField(blank=True, null=True)),
                ('sirketlesme_tamamlandi_mi', models.BooleanField(blank=True, default=False, null=True)),
                ('fatura_kesiliyor_mu', models.BooleanField(blank=True, default=False, null=True)),
                ('calisma_durumu', models.BooleanField(blank=True, default=False, null=True)),
                ('company_purchasing_merging', models.BooleanField(blank=True, default=False, null=True)),
                ('sirket_borsaya_acildi_mi', models.BooleanField(blank=True, default=False, null=True)),
                ('girisim_mentorluk_ihtiyac_alanlari', models.CharField(choices=[('B2B', 'B2B'), ('B2C', 'B2C'), ('Basın', 'Basın'), ('Big Data', 'Big Data'), ('C2C', 'C2C'), ('Dağıtım', 'Dağıtım'), ('Denetim', 'Denetim'), ('Devlet İle İlişkiler', 'Devlet İle İlişkiler'), ('Donanım', 'Donanım'), ('Dış Ticaret', 'Dış Ticaret'), ('Dijital Pazarlama', 'Dijital Pazarlama'), ('E-Ticaret', 'E-Ticaret'), ('Fikir Doğrulama', 'Fikir Doğrulama'), ('Fiyatlandırma', 'Fiyatlandırma'), ('Fon Bulma', 'Fon Bulma'), ('Growth Hacking', 'Growth Hacking'), ('Gümrük', 'Gümrük'), ('Halkla İlişkiler', 'Halkla İlişkiler'), ('Hibe ve Destekler', 'Hibe ve Destekler'), ('Hukuk', 'Hukuk'), ('IoT', 'IoT'), ('IT', 'IT'), ('İnovasyon', 'İnovasyon'), ('İnsan Kaynakları', 'İnsan Kaynakları'), ('İçerik Pazarlama', 'İçerik Pazarlama'), ('İş Geliştirme', 'İş Geliştirme'), ('İş Modeli', 'İş Modeli'), ('İş Yönetimi', 'İş Yönetimi'), ('Kalite Yönetimi', 'Kalite Yönetimi'), ('Kitlesel Fonlama', 'Kitlesel Fonlama'), ('Liderlik', 'Liderlik'), ('Marka', 'Marka'), ('Muhasebe', 'Muhasebe'), ('Müşteri İlişkileri', 'Müşteri İlişkileri'), ('Patent', 'Patent'), ('Pazar Araştırması', 'Pazar Araştırması')], max_length=40)),
                ('girisim_ozeti', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=800)])),
                ('yatirimci_sunumu', models.FileField(blank=True, default='', null=True, upload_to='yatirimci_sunumu/')),
                ('finansman_kullanildi_mi', models.BooleanField(blank=True, default=False, null=True)),
                ('son_finansman_tarihi', models.DateField(blank=True, null=True)),
                ('son_finansman_turu', models.CharField(blank=True, max_length=254, null=True)),
                ('son_finansman_miktari', models.PositiveBigIntegerField(blank=True, null=True)),
                ('toplam_finansman_miktari', models.PositiveBigIntegerField(blank=True, null=True)),
                ('ekip_arkadasi_adi', models.CharField(blank=True, max_length=80, null=True)),
                ('ekip_arkadasi_soyadi', models.CharField(blank=True, max_length=80, null=True)),
                ('ekip_arkadasi_email', models.CharField(blank=True, max_length=80, null=True)),
                ('ekip_arkadasi_telefonu', models.CharField(blank=True, max_length=10, null=True)),
                ('ekip_arkadasi_linkedin', models.URLField(blank=True, null=True)),
                ('ekip_arkadasi_departmani', models.CharField(blank=True, choices=[('Mühendislik / Engineering', 'Mühendislik / Engineering'), ('Yönetim / Management', 'Yönetim / Management'), ('Ürün / Product', 'Ürün / Product'), ('Finans / Finance', 'Finans / Finance'), ('İnsan Kaynakları / Human Resources', 'İnsan Kaynakları / Human Resources'), ('Bilgi Teknolojisi / Information Technology', 'Bilgi Teknolojisi / Information Technology'), ('Hukuk / Legal', 'Hukuk / Legal'), ('Pazarlama / Marketing', 'Pazarlama / Marketing'), ('Tıp ve Bilim / Medical & Science', 'Tıp ve Bilim / Medical & Science'), ('Operasyonel / Operations', 'Operasyonel / Operations'), ('Profesyonel Hizmetler / Pro Services', 'Profesyonel Hizmetler / Pro Services'), ('Satış / Sales', 'Satış / Sales'), ('Destek / Support', 'Destek / Support')], max_length=80, null=True)),
                ('ekip_arkadasi_calistigi_pozisyon', models.CharField(blank=True, choices=[('Asistan / Assistant', 'Asistan / Assistant'), ('Ortak / Partner', 'Ortak / Partner'), ('Direktör, Operasyonlar / Director, Operations', 'Direktör, Operasyonlar / Director, Operations'), ('Kıdemli Direktör / Senior Director', 'Kıdemli Direktör / Senior Director'), ('Profesör / Professor', 'Profesör / Professor'), ('Danışman / Consultant', 'Danışman / Consultant'), ('Koordinatör / Coordinator', 'Koordinatör / Coordinator'), ('Kıdemli Başkan Yardımcısı / Senior Vice President', 'Kıdemli Başkan Yardımcısı / Senior Vice President'), ('Genel Müdür / General Manager', 'Genel Müdür / General Manager'), ('Sahibi / Owner', 'Sahibi / Owner'), ('Program Yöneticisi / Program Manager', 'Program Yöneticisi / Program Manager'), ('CEO / CEO', 'CEO / CEO'), ('Yönetici, Operasyonlar / Manager, Operations', 'Yönetici, Operasyonlar / Manager, Operations'), ('Hesap Yöneticisi / Account Manager', 'Hesap Yöneticisi / Account Manager'), ('Yönetici, Satış / Manager, Sales', 'Yönetici, Satış / Manager, Sales'), ('Mühendis / Engineer', 'Mühendis / Engineer'), ('Başkan / President', 'Başkan / President'), ('Süpervizör / Supervisor', 'Süpervizör / Supervisor'), ('Proje Yöneticisi / Project Manager', 'Proje Yöneticisi / Project Manager'), ('Yönetmen / Director', 'Yönetmen / Director'), ('Üst Düzey Yönetici / Executive', 'Üst Düzey Yönetici / Executive'), ('Başkan Yardımcısı / Vice President', 'Başkan Yardımcısı / Vice President'), ('Yönetici / Manager', 'Yönetici / Manager'), ('Analist / Analyst', 'Analist / Analyst')], max_length=80, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Girişim',
                'verbose_name_plural': 'Girişimler',
                'db_table': 'girisim',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='GirisimGelismelerHedefler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gelisme_veya_hedef_tarihi', models.DateField(blank=True, null=True)),
                ('gelisme_veya_hedef_aciklamasi', models.CharField(max_length=240)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'girisimGelismelerHedefler',
                'verbose_name_plural': 'girisimGelismelerHedefleri',
                'db_table': 'girisimGelismelerHedefler',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='GirisimHaberleri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haber_tarihi', models.DateField()),
                ('haber_basligi', models.CharField(max_length=255)),
                ('haber_linki', models.URLField()),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'GirisimHaberi',
                'verbose_name_plural': 'GirisimHaberleri',
                'db_table': 'girisimHaberleri',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='GirisiminYatirimTurlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_tipi', models.CharField(choices=[('Pre-Seed', 'Pre-Seed'), ('Seed', 'Seed'), ('Seri A', 'Sei A')], default='Pre-Seed', max_length=10)),
                ('round_tutari', models.PositiveBigIntegerField()),
                ('sirketin_degeri', models.PositiveBigIntegerField()),
                ('yatirim_turu_baslangic_tarihi', models.DateField()),
                ('yatirim_turu_bitis_tarihi', models.DateField()),
                ('yatirim_turu_aktif_veya_eski', models.CharField(choices=[('Aktif Yatırım Turu', 'Aktif Yatırım Turu'), ('Eski Yatırım Turu', 'Eski Yatırım Turu')], default='Aktif Yatırım Turu', max_length=20)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'GirisimYatirimi',
                'verbose_name_plural': 'GirisimYatirimlari',
                'db_table': 'girisiminYatirimTurlari',
                'ordering': ['-pk'],
            },
        ),
    ]
