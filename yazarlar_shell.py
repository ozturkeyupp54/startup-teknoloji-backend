import os
import pandas as pd
import django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from post.models import Post
from django.db import transaction
from django.utils.text import slugify
from unidecode import unidecode

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startup.settings')
django.setup()

# CSV dosyasını oku
df = pd.read_csv('Post-2024-02-19.csv')

# Eşleştirme yapılacak yazarlar
eşleştirilecek_yazarlar = [
    'ENES EMRE KILINÇ',
    'BERKAY YENİDÜNYA',
    'BERNA DİLEK',
    'AHSEN YAĞLI',
    'ZEKİ TALUSTAN GÜLTEN',
    'EGEHAN GÜNGÖR',
    'HASRET GÖNÜLTAŞ',
    'ESRA TUZCUOĞLU',
    'AYŞIN DEMİRER',
    'ERKAN UZUNOĞLU',
    'FATİH KILIÇ',
    'HAKAN KAPAKLI',
    'HAMDI KÜÇÜK',
    'HASAN SALHI',
    'ÖMÜRDEN SEZGİN',
    'SADIK VURAL',
    'SERHAT DUYAR',
    'SERKAN BEYAZ',
    'SINAN PEKSOY',
    'ŞULE TÜRKYILMAZ',
    'UMMAN AÇIKGÖZ ÖNCAN',
    'UTKU ASKER',
    'UĞUR YILDIZ',
    'VEYIS ÖZEN ERTUĞ',
    'YASIN NAZLIGÜL',
    'ZAFER TARHAN',
    'SEMANUR BAT',
    'ÖZCAN KAMANLI',
    'ÖMER YURTDAŞ',
    'OĞUZHAN GEZEN',
    'MUSTAFA ÜNAL',
    'METIN GÜNER',
    'MERVE BAHAR',
    'MEHMET BEHNAN TÜRKERI',
    'KAIS AKRAM',
    'İREM YAĞMUR KESKIN',
    'İREM IRMAK',
    'İLKAY BOZ',
    'İBRAHIM EGE',
    'GÜNCE ONUR',
    'GULCAN UYANIKER',
    'GIZEM ÇELIK',
    'EZGI TEKIN',
    'EROL KÜÇÜKKAYA',
    'ENES YİĞİT',
    'ELIF ERDAL',
    'ELIF BORAL TAŞDEMIR',
    'EDA GEYIK',
    'CEMIL KAĞAN GÜRKAN',
    'CAN MUTLU',
    'ABDULLAH ŞAŞKIN',
    'MERVE MUTLU',
    'STARTUPTEKNOLOJI',
    'ISA UYSAL',
    'ILKER ELAL',
]

# Eşleştirme yapılacak yazarların slug'larını oluştur
eşleştirilecek_yazarlar_slug = [slugify(yazar) for yazar in eşleştirilecek_yazarlar]


# Manuel olarak eşleştirme yap
manuel_eslesme = {
    'Aysin': 'AYŞIN DEMİRER',
    'bernadilek': 'BERNA DİLEK',
    'enesemreklnc': 'ENES EMRE KILINÇ',
    'fatihkilic': 'FATİH KILIÇ',
    'hakankapakli': 'HAKAN KAPAKLI',
    'handekaya': 'HANDE KAYA',
    'Hande': 'HANDE KAYA',
    'hasansalhi':  'HASAN SALHI',
    'Hilal Barin':  'HİLAL BARİN',
    'Hilal':  'HİLAL BARİN',
    'huuseyinceylan':  'HÜSEYİN CEYLAN',
    'ilkerelal':  'İLKER ELAL',
    'iremkeskin1':  'İREM YAĞMUR KESKIN',
    'irem':  'İREM IRMAK',
    'isauysal':  'İSA UYSAL',
    'mehmetbenhan':   'MEHMET BENHAN TÜRKERI',
    'serhatduyar':   'SERHAT DUYAR',
    'startup teknoloji':   'STARTUPTEKNOLOJI',
    'sadikvural': 'SADIK VURAL',
    'omurdensezgin': 'ÖMÜRDEN SEZGİN',
    'ibrahimege': 'İBRAHIM EGE',
    'hasretgonultas': 'HASRET GÖNÜLTAŞ',
    'eyupozturk': 'EYÜP ÖZTÜRK',
    'emrekiraz': 'EMRE KİRAZ',
    'enesyigit': 'ENES YİĞİT',
    'Elif': 'ELİF SERAN TUN',
    'Elif Seran Tun': 'ELİF SERAN TUN',
    'Ceyda Yarkent': 'CEYDA YARKENT',
    'Ceyda': 'CEYDA YARKENT',
    'Cansu Cetinkaya': 'CANSU ÇETİNKAYA',
    'Can': 'CAN MUTLU',
    'canmutlu': 'CAN MUTLU',
    'busrakorkmaz': 'BÜŞRA KORKMAZ',
    'byzpnarr': 'BEYZA PINAR',
    'Beyza': 'BEYZA PINAR',
    'berkaykilicaslan': 'BERKAY KILIÇASLAN',
    'berfinnamli': 'BERFİN NAMLI',
    'berke_yasar': 'BERKE YAŞAR',
    'bariskorkmaz': 'BARIŞ KORKMAZ',
    'azrayildirim': 'AZRA YILDIRIM',
    'zafertarhan': 'ZAFER TARHAN',
    'Aytuncuysal': 'AYTUNC UYSAL',
    'Dilay KOT': 'DİLAY KOT',
    'Emine Yalcin': 'EMİNE YALÇIN',
    'Ertugrul': 'ERTUĞRUL KORKMAZ',
    'Ertugrul KORKMAZ': 'ERTUĞRUL KORKMAZ',
    'GokhanTASKIN': 'GÖKHAN TAŞKIN',
    'MehmetBaranKilic': 'MEHMET BARAN KILIÇ',
    'Pelda Yalcinkaya': 'PELDA YALÇINKAYA',
    'tubakaya': 'TUBA KAYA',
    'sinanpeksoy': 'SİNAN PEKSOY',
    'tolgacelik1923': 'TOLGA ÇELİK',
    'oguzhangezen': 'OĞUZHAN GEZEN',
    'mustafatarcan': 'MUSTAFA TARCAN',
    '@nuryilmaz': 'NUR YILMAZ',
    'Dilek Yilmaz': 'DİLEK YILMAZ',
    'Sena Kurkcu': 'SENA KÜRKÇÜ',
    'Tayfur Bal': 'TAYFUR BAL',
    'Buse': 'BUSE YILMAZ',
    'utkuasker': 'UTKU ASKER',
    'suleturkyilmaz': 'ŞULE TÜRK YILMAZ',
    'Neslihan Aytekin': 'NESLİHAN AYTEKİN',
    
    # Manuel eşleştirmeleri buraya ekleyin
}


# Eşleşen yazarı bulan fonksiyon
def bulunan_yazar(creator):
    # Check for manual matches first
    if creator in manuel_eslesme:
        return slugify(unidecode(manuel_eslesme[creator])).upper()

    # Continue with default matching logic
    creator_slug = slugify(unidecode(creator))
    
    for yazar_slug in eşleştirilecek_yazarlar_slug:
        if yazar_slug in creator_slug:
            return yazar_slug
    return None

@transaction.atomic
def update_post_creator(row):
    # Eşleşen yazarı bul
    eslesen_yazar_slug = bulunan_yazar(row['creator'])
    
    # Post objesini al
    try:
        post = Post.objects.get(pk=row['id'])
    except ObjectDoesNotExist:
        post = None
    
    # Eğer post objesi varsa ve eşleşen yazar bulunmuşsa, creator alanını güncelle
    if post and eslesen_yazar_slug is not None:
        # Türkçe karakterleri büyük harfe dönüştür
        eslesen_yazar_buyuk = unidecode(eslesen_yazar_slug.replace('-', ' ')).upper()
        
        # Güncelleme yapmadan önce mevcut creator'ı kontrol et
        if post.creator != eslesen_yazar_buyuk:
            # Eğer mevcut creator eşleşen yazar değilse, güncelle
            post.creator = eslesen_yazar_buyuk
            post.save()
            
            # Print ekleyerek güncelleme bildirisi yap
            print(f'Updated creator for post: {post.title} - New creator: {eslesen_yazar_buyuk}')
    else:
        # Eğer eşleşen yazar bulunamazsa, mevcut creator'ı "STARTUPTEKNOLOJİ" olarak değiştir
        new_creator = 'STARTUPTEKNOLOJI'
        if post.creator != new_creator:
            post.creator = new_creator
            post.save()
            print(f'No match found for post: {post.title} - Setting creator to: {new_creator}')
        else:
            print(f'No match found for post: {post.title} - Keeping existing creator: {post.creator}')

# Her bir satır için işlemi gerçekleştir
df.apply(update_post_creator, axis=1)

