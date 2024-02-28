# startup-teknoloji-backend

# "startup-teknoloji-backend" klasöründe terminal açıp sırasıyla aşağıdaki komutları terminalde çalıştırıyoruz. 


# İLK KURULUM (github'dan repo lokal bilgisayara çekildikten sonra ilk kurulum için gerekli komutlar)

python -m venv env

source env/scripts/activate

# terminalde klasör yolunun üzerinde " (env) " şeklinde environment ortamında çalışmaya başladığımız göreceğiz. 

pip install django

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

# admin oluşturuyoruz

python manage.py createsuperuser

# username: admin
# email: BOŞ BIRAKALIM
# password: HER ZAMAN HATIRLAYACAĞINIZ KOLAY BİR ŞİFRE OLABİLİR (2 KERE GİRİLECEK)
# ŞİFRE KOLA BİR ŞİFRE OLDU SORUSUNA "YES" DEYİP ADMİN KULLANICISINI OLUŞTURUYORUZ.



# SONRA SERVER'I ÇALIŞTIRIYORUZ

python manage.py runserver


### *************************************

# B. İKİNCİ VE DEVAMINDAKİ SERVER'I ÇALIŞTIRMADA KULLANILACAK TERMİNAL KOMUTLARI

# github'dan repoyu güncelledikten sornra, "startup-teknoloji-backend" klasöründe terminal açıp sırasıyla aşağıdaki komutları terminalde çalıştırıyoruz. 

source env/scripts/activate

# terminalde klasör yolunun üzerinde " (env) " şeklinde environment ortamında çalışmaya başladığımız göreceğiz. 

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

 