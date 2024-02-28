from django.db import models
from django.core.validators import MaxLengthValidator
from user.models import User

from utils.utils import turkish_slugify

class Author(models.Model):
    class Meta:
        db_table = 'author'
        verbose_name = 'Yazar'
        verbose_name_plural = 'Yazarlar'
        ordering = ['-pk']
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='author_profile_pictures/', default='')
    bio = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(limit_value=600)])
    slug = models.SlugField(max_length=255, blank=True, null=True)
    yazarin_linkedin_adresi_linki = models.URLField(blank=True, null=True)
    yazarin_instagram_adresi_linki = models.URLField(blank=True, null=True)
    yazarin_twitter_x_adresi_linki = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.full_name
 
        
    def save(self, user_instance=None, *args, **kwargs):
        
        if user_instance:
            self.user = user_instance
        elif not self.user:
            self.user = User.objects.get(username='default_user', full_name='STARTUPTEKNOLOJİ', email='iletisim@startupteknoloji.com')
        
        if self.user.first_name and self.user.last_name:
            self.full_name = "%s %s" % (self.user.first_name, self.user.last_name)
        else:
            self.full_name = ""        
        
        if self.pk is not None:
            orig = Author.objects.get(pk=self.pk)
            if orig.slug != turkish_slugify(self.full_name):
                self.slug = turkish_slugify(self.full_name)
        else:
            self.slug = turkish_slugify(self.full_name)

        super(Author, self).save(*args, **kwargs)
