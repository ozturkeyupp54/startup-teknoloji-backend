import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startup.settings')
django.setup()

from post.models import Post

def upload_post_images():
    extensions = ['.jpeg', '.jpg', '.png']  # Kontrol edilecek dosya uzantıları
    default_image_path = os.path.join(settings.MEDIA_ROOT, 'default', 'startupteknoloji-default.png')  # Default resim yolu
    default_relative_path = 'default/startupteknoloji-default.png'  # Veritabanına kaydedilecek default resim yolu
    for post in Post.objects.all():
        slug = post.slug
        found = False
        for ext in extensions:
            image_path = os.path.join(settings.MEDIA_ROOT, 'haber_baslik_resmi', 'baslikresimleri', f'{slug}{ext}')
            if os.path.exists(image_path):
                relative_path = f'haber_baslik_resmi/baslikresimleri/{slug}{ext}'
                post.haber_baslik_resmi = relative_path
                post.save()
                print(f'Updated image for post: {post.title}')
                found = True
                break  # Dosya bulundu, döngüden çık
        if not found:
            # Eğer resim bulunamazsa, default resimi atayın
            post.haber_baslik_resmi = default_relative_path
            post.save()
            print(f'Default image set for post: {post.title}')

upload_post_images()