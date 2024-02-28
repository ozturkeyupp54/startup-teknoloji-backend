import os
import pandas as pd
import django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from post.models import Post
from category.models import Category
from django.db import transaction
from django.utils.text import slugify
from unidecode import unidecode

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startup.settings')
django.setup()

# CSV dosyasını oku
df = pd.read_csv('Post-2024-02-19.csv')

# Eşleştirme yapılacak kategoriler
eşleştirilecek_kategoriler = [
    'YATIRIM HABERLERİ', 'AKILLI CİHAZLAR', 'DONANIM', 'DUYURU HABERLERİ',
    'MARKA İŞ BİRLİKLERİ', 'STARTUP TANITIM', 'YENİ NESİL ŞİRKETLER', 'STARTUP RAPORLARI',
    'GİRİŞİM HIZLANDIRMA PROGRAMLARI', 'RÖPORTAJ', 'EĞİTİM', 'RAPOR VE İNCELEME', 'SOSYAL GİRİŞİMCİLİK',
    'BLOCKCHAIN', 'APPLE', 'ANDROID', 'OTOMOTİV', 'YAPAY ZEKA', 'UZAY VE HAVACILIK', 'SİBER GÜVENLİK',
    'E-TİCARET', 'UYGULAMALAR', 'OYUN DÜNYASI', 'SOSYAL MEDYA', 'FİLM VE DİZİ',
]

# Eşleştirme yapılacak kategorilerin hepsini küçük harfe çevir
eşleştirilecek_kategoriler_slug = [slugify(kategori) for kategori in eşleştirilecek_kategoriler]


# Manuel olarak eşleştirme yap
manuel_eslesme = {
    'Yatırım Haberleri': 'YATIRIM HABERLERİ',
    'Startup Tanıtım': 'STARTUP TANITIM',
    'Startup Raporları': 'STARTUP RAPORLARI',
    'Girişim Hızlandırma Programları': 'GİRİŞİM HIZLANDIRMA PROGRAMLARI',
    'Akıllı Cihazlar': 'AKILLI CİHAZLAR',
    'Donanım': 'DONANIM',
    'Uzay Havacılık': 'UZAY VE HAVACILIK',
    # Manuel eşleştirmeleri buraya ekleyin
}


# Eşleşen kategoriyi bulan fonksiyon
def bulunan_kategori(categories):
    # Check for manual matches first
    if categories in manuel_eslesme:
        return slugify(unidecode(manuel_eslesme[categories])).upper()
    
    
  # Continue with default matching logic
    categories_slug = slugify(unidecode(categories))
    
    for kategori_slug in eşleştirilecek_kategoriler_slug:
        if kategori_slug in categories_slug:
            return kategori_slug
    return None

@transaction.atomic
def update_post_category(row):
    # Eşleşen kategoriyi bul
    eslesen_kategori_slug = bulunan_kategori(row['categories'])
    
    # Post objesini al
    try:
        post = Post.objects.get(pk=row['id'])
    except ObjectDoesNotExist:
        post = None
    
    # Eğer post objesi varsa ve eşleşen kategori bulunmuşsa, category alanını güncelle
    if post and eslesen_kategori_slug:
        # Türkçe karakterleri büyük harfe dönüştür
        eslesen_kategori_buyuk = unidecode(eslesen_kategori_slug.replace('-', ' ')).upper()
        
        # Kategoriyi oluştur veya al
        category, _ = Category.objects.get_or_create(name=eslesen_kategori_buyuk)
        
        # Kategoriye bağlı olan postu güncelle
        post.category = category
        post.save()
        
        # Print ekleyerek güncelleme bildirisi yap
        print(f'Updated category for post: {post.title} - New category: {eslesen_kategori_buyuk}')
    else:
        # Eğer eşleşen kategori bulunamazsa, varsayılan kategori olan "GİRİŞİMCİLİK" kullanılır
        default_category, _ = Category.objects.get_or_create(name='GIRISIMCILIK')
        post.category = default_category
        post.save()
        
        # Print ekleyerek güncelleme bildirisi yap
        print(f'Updated category for post: {post.title} - Default category: GIRISIMCILIK')

# Her bir satır için işlemi gerçekleştir
df.apply(update_post_category, axis=1)
