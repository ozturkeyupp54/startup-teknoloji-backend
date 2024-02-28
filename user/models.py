from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.utils import turkish_slugify

class User(AbstractUser):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-pk']
        app_label = 'user'
        
    EGITIM_SEVIYESI = [
      ('İlkokul', 'İlkokul'),
      ('Ortaokul', 'Ortaokul'),
      ('Lise', 'Lise'),
      ('Lisans', 'Lisans'),
      ('Yüksek Lisans', 'Yüksek Lisans'),
      ('Doktora', 'Doktora')
    ]
    
    first_name = models.CharField(max_length=35, blank=True, null=True)
    last_name = models.CharField(max_length=35, blank=True, null=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='user_profile_pictures/', default='', blank=True, null=True)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=10, default="8503070535", verbose_name="Phone")
    
    linkedin_profiliniz = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=254, blank=True, null=True)
    sirket_adi = models.CharField(max_length=254,unique=True,blank=True, null=True)
    dogum_gununuz = models.DateField(blank=True,null=True)
    egitim_seviyesi=models.CharField(max_length=15, choices=EGITIM_SEVIYESI,blank=True,null=True)

    tckn = models.CharField(max_length=11, default="00000000000", blank=True, null=True)
    kvkk = models.BooleanField(default=False, blank=True, null=True)  # KVKK sözleşmesi
    is_membership = models.BooleanField(default=False, null=True, blank=True)  # Üyelik sözleşmesi
    is_electronic_commerce = models.BooleanField(default=False, null=True, blank=True)  # Elektronik ticaret sözleşmesi

    is_staff = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    login_attempt = models.IntegerField(default=0, null=True, blank=True)
    is_verified = models.BooleanField(default=False, null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        First_name ve last_name arasında boşluk bırakarak döndürün.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def save(self, *args, **kwargs):
            # first_name ve last_name varsa, büyük harfe dönüştür
            if self.first_name:
                self.first_name = self.first_name.upper()
            if self.last_name:
                self.last_name = self.last_name.upper()

            # full_name'i güncelle
            if self.first_name and self.last_name:
                self.full_name = "%s %s" % (self.first_name, self.last_name)
            else:
                self.full_name = ""

            # slug'ı güncelle
            if self.pk is not None:
                orig = User.objects.get(pk=self.pk)
                if orig.slug != turkish_slugify(self.full_name):
                    self.slug = turkish_slugify(self.full_name)
            else:
                self.slug = turkish_slugify(self.full_name)

            super(User, self).save(*args, **kwargs)