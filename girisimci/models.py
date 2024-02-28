from django.db import models
from django.core.validators import MaxLengthValidator
from user.models import User
from utils.utils import turkish_slugify

class Girisimci(models.Model):
    class Meta:
        db_table = 'girisimci'
        verbose_name = 'Girişimci'
        verbose_name_plural = 'Girişimciler'
        ordering = ['-pk']
    
    EGITIM_SEVIYESI = [
      ('İlkokul', 'İlkokul'),
      ('Ortaokul', 'Ortaokul'),
      ('Lise', 'Lise'),
      ('Lisans', 'Lisans'),
      ('Yüksek Lisans', 'Yüksek Lisans'),
      ('Doktora', 'Doktora')
      ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='')
    linkedin_profiliniz = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(limit_value=1000)])
    slug = models.SlugField(max_length=254, blank=True, null=True)
    sirket_adi = models.CharField(max_length=254,unique=True)
    dogum_gununuz = models.DateField(blank=True,null=True)
    egitim_seviyesi=models.CharField(max_length=15, choices=EGITIM_SEVIYESI,blank=True,null=True)

    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
            return f" {self.full_name} - {self.sirket_adi} "

    def save(self, *args, **kwargs):
        if self.user.first_name and self.user.last_name:
            self.full_name = "%s %s" % (self.user.first_name, self.user.last_name)
        else:
            self.full_name = ""        
        
        if self.pk is not None:
            orig = Girisimci.objects.get(pk=self.pk)
            if orig.slug != turkish_slugify(self.full_name):
                self.slug = turkish_slugify(self.full_name)
        else:
            self.slug = turkish_slugify(self.full_name)

        super(Girisimci, self).save(*args, **kwargs)   

