# from datetime import datetime
# from post.models import Post
# from django.core.files import File
# import os

# # Var olan tüm haberleri alın
# all_posts = Post.objects.all()

# # Her bir haber için işlem yapın
# for post in all_posts:
#     # pub_date alanını kontrol edin
#     if post.pub_date:
#         # pub_date alanını datetime nesnesine çevirin
#         pub_date_str = post.pub_date
#         pub_date_obj = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S +0000')

#         # İlgili yıl ve ayı belirleyin
#         year = pub_date_obj.year
#         month = pub_date_obj.month

#         # İlişkili resmin dosya yolunu belirtin
#         file_path_1 = f'wp-content/uploads/{year}/{month:02d}/{post.slug}.jpg'
#         file_path_2 = f'wp-content/uploads/{year}/{month:02d}/{post.slug}-StartupTeknoloji-1.jpg'

#         # Her iki durumu kontrol et
#         if not os.path.exists(file_path_1) and not os.path.exists(file_path_2):
#             print(f"Dosya bulunamadı: {file_path_1} ve {file_path_2}")
#             continue

#         # Dosya yolu üzerinden File nesnesi oluşturun
#         with open(file_path_1 if os.path.exists(file_path_1) else file_path_2, 'rb') as file:
#             post.haber_baslik_resmi.save(os.path.basename(file_path_1), File(file))

#         # Haberi kaydedin
#         post.save()
#     else:
#         print(f"post.id={post.id} için pub_date değeri bulunamadı.")


from post.models import Post
from django.core.files import File
import os
from datetime import datetime

# Var olan tüm haberleri alın
all_posts = Post.objects.all()

# Her bir haber için işlem yapın
for post in all_posts:
    # pub_date alanını kontrol edin
    if post.pub_date:
        # pub_date alanını kullanarak dosya değiştirme tarihini alın
        pub_date_str = post.pub_date
        pub_date_obj = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S +0000')
        # İlgili yıl ve ayı belirleyin
        year = pub_date_obj.year
        month = pub_date_obj.month

        # Dosya adını belirleyin (örneğin, jpg dosyalarını içeren bir klasör)
        folder_path = f'wp-content/uploads/{year}/{month:02d}/'

        # Dosya değiştirme tarihine en yakın dosyayı bulun
        closest_file = None
        closest_diff = float('inf')  # Sonsuz büyük bir başlangıç değeri

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            print(f"Dosya Yolu: {file_path}")

            # Dosyanın değiştirme tarihini alın
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            # İki tarih arasındaki farkı hesaplayın
            time_diff = abs((pub_date_obj - file_mod_time).total_seconds())

            # Şu ana kadar en yakın dosyayı bulun
            if time_diff < closest_diff:
                closest_diff = time_diff
                closest_file = file_path

        # En yakın dosya bulundu mu kontrol et
        if closest_file:
            # Dosya yolu üzerinden File nesnesi oluşturun
            with open(closest_file, 'rb') as file:
                post.haber_baslik_resmi.save(os.path.basename(closest_file), File(file))

            # Haberi kaydedin
            post.save()
        else:
            print(f"post.id={post.id} için uygun dosya bulunamadı.")
    else:
        print(f"post.id={post.id} için pub_date değeri bulunamadı.")

# from post.models import Post
# from django.core.files import File
# import os
# from datetime import datetime

# # Var olan tüm haberleri alın
# all_posts = Post.objects.all()

# # Her bir haber için işlem yapın
# for post in all_posts:
#     # pub_date alanını kontrol edin
#     if post.pub_date:
#         # pub_date alanını kullanarak dosya değiştirme tarihini alın
#         pub_date_str = post.pub_date
#         pub_date_obj = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S +0000')
#         # İlgili yıl ve ayı belirleyin
#         year = pub_date_obj.year
#         month = pub_date_obj.month

#         # Dosya adını belirleyin (örneğin, jpg dosyalarını içeren bir klasör)
#         folder_path = f'wp-content/uploads/{year}/{month:02d}/'
        

#         # Dosya adını belirleyin
#         file_name = f'*.jpg'
#         file_path = os.path.join(folder_path, file_name)

#         # Dosyanın varlığını kontrol et
#         if os.path.exists(file_path):
#             # Dosya yolu üzerinden File nesnesi oluşturun
#             with open(file_path, 'rb') as file:
#                 post.haber_baslik_resmi.save(os.path.basename(file_path), File(file))

#             # Haberi kaydedin
#             post.save()
#         else:
#             print(f"post.id={post.id} için uygun dosya bulunamadı.")
#     else:
#         print(f"post.id={post.id} için pub_date değeri bulunamadı.")
