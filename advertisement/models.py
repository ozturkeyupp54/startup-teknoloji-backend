from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from user.models import User

class Advertisement(models.Model):
  
    class Meta:
          db_table = 'advertisement'
          verbose_name = 'Advertisement'
          verbose_name_plural = 'Advertisements'
          ordering = ['-pk']

    REKLAM_GOSTERIM_YERI = [
      ('Üst', 'Üst'),
      ('Alt', 'Alt'),
      ('Her İkiside', 'Her İkiside')
    ]


    kampanya_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    kampanya_creator_adi=models.CharField(max_length=255)
    kampanya_creator_soyadi=models.CharField(max_length=255)
    kampanya_basligi = models.CharField(max_length=255, unique=True)
    sirket_adi = models.CharField(max_length=255)
    kampanya_baslangic_tarihi = models.DateField()
    kampanyanin_websitesinin_linki = models.URLField()   
        
    advertisement_ust_resmi = ProcessedImageField(
        upload_to='anasayfa_ust_taraf_reklam_resmi/',
        processors=[ResizeToFill(1250, 250)],
        format='JPEG',
        options={'quality': 80},
        blank=True,
        null=True,
    )
    
    

    advertisement_ust_resmi_views = models.PositiveIntegerField(default=0)
    reklam_gosterim_yeri = models.CharField(max_length=15,default = 'Üst')    
    max_views_per_image = models.PositiveIntegerField(default=100, null=True, blank=True)    

    is_active = models.BooleanField(default=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f" {self.kampanya_creator} {self.kampanya_basligi} "

    def get_advertisements_by_creator(self, advertisement_creator ):
        """
        Get all posts by a specific creator.
        """
        return Advertisement.objects.filter(advertisement_creator=advertisement_creator , is_active=True, is_deleted=False)
    

    def increment_views(self, image_field_name):
        if self.max_views_per_image is not None:
            # Check if the view count for the image has reached the limit
            view_count_field_name = f"{image_field_name}_views"
            setattr(self, view_count_field_name, getattr(self, view_count_field_name) + 1)
            self.save(update_fields=[view_count_field_name])

            if getattr(self, view_count_field_name) >= self.max_views_per_image:
                    # Set a default image path instead of deleting the image
                    default_image_path = 'default/default_reklam_resmi.jpg'
                    setattr(self, image_field_name, default_image_path)
                    self.save(update_fields=[image_field_name])
        else:
            # No limit set, increment views normally
            super().increment_views(image_field_name)


    def save(self, *args, **kwargs):
        # Convert fields to uppercase before saving
        self.kampanya_creator_adi = self.kampanya_creator_adi.upper() if self.kampanya_creator_adi else None
        self.kampanya_creator_soyadi = self.kampanya_creator_soyadi.upper() if self.kampanya_creator_soyadi else None
        self.kampanya_basligi = self.kampanya_basligi.upper() if self.kampanya_basligi else None
        self.sirket_adi = self.sirket_adi.upper() if self.sirket_adi else None

        # Varsayılan resim dosyasının yolu
        # default_image_path = 'default/default_reklam_resmi.jpg'

        # Sadece 'Her İkiside' seçiliyse her iki resmi de kaydet
        # if self.reklam_gosterim_yeri == 'Her İkiside':
        #     super().save(*args, **kwargs)
        # # Sadece 'Üst' seçiliyse sadece üst resmi kaydet
        # elif self.reklam_gosterim_yeri == 'Üst':
        #     if self.advertisement_alt_resmi:
        #         self.advertisement_alt_resmi = None
        #     # Alt resmi None yapmadan önce varsayılan resmi atayın
        #     self.advertisement_alt_resmi = None  # Set to None to keep it empty
        #     super().save(*args, **kwargs)
        # # Sadece 'Alt' seçiliyse sadece alt resmi kaydet
        # elif self.reklam_gosterim_yeri == 'Alt':
        #     if self.advertisement_ust_resmi:
        #         self.advertisement_ust_resmi = None
        #     # Üst resmi None yapmadan önce varsayılan resmi atayın
        #     self.advertisement_ust_resmi = None
        super().save(*args, **kwargs)

