from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from meta.models import ModelMeta
from django.urls import reverse
from category.models import Category
from author.models import Author
from utils.utils import turkish_slugify

class Post(ModelMeta, models.Model):
    
    STATUS = (
        ('Taslak', 'Taslak'),
        ('Yayinda', 'Yayinda')
    )
    
    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-pk']


    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank= True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', blank= True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    content = CKEditor5Field('Text', config_name='extends')    
    haber_baslik_resmi = models.ImageField(max_length=255, upload_to='haber_baslik_resmi/', default='/haber_baslik_resmi/startupteknoloji-default.png', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    publish_date = models.DateTimeField(auto_now=True) 
    pub_date = models.CharField(max_length=255,blank=True, null=True)
    # post_date = models.CharField(max_length=255,blank=True, null=True)
    post_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    yayimlanma_durumu = models.CharField(max_length=10, choices=STATUS, default='Taslak')
    post_views_count = models.CharField(max_length=255,blank=True, null=True)
    copyrightYear = models.DateField(auto_now=True,blank=True, null=True)
    metadesc = models.TextField(blank=True, null=True)
    focuskeywords = models.CharField(max_length=255,blank=True, null=True)
    keywordsynonyms = models.CharField(max_length=255,blank=True, null=True)

    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    _metadata = {
        'title': 'title',
        'description': 'content',
        'haber_baslik_resmi': 'get_meta_image',
        'focuskeywords': 'keywords'
    }
    _schema = {
        'haber_baslik_resmi': 'get_image_full_url',
        'content': 'text',
        'categories': 'get_categories',
        'creator': 'get_schema_author',
        'copyrightYear': 'copyright_year',
        'created_at': 'get_date',
        'publish_date': 'get_date',
        'pub_date': 'date_published',
        'headline': 'headline',
        'keywords': 'get_keywords',
        'description': 'get_description',
        'title': 'title',
        'url': 'get_full_url',
        'mainEntityOfPage': 'get_full_url',
        'publisher': 'get_site',
    }
    
    def get_meta_image(self):
        if self.haber_baslik_resmi:
            return self.haber_baslik_resmi

    def __str__(self):
        return f" {self.title} "


    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Post.objects.get(pk=self.pk)
            if orig.title != self.title:
                self.slug = turkish_slugify(self.title)
        else:
            self.slug = turkish_slugify(self.title)
            
        if self.author:
            self.creator = self.author.full_name
        else:
            self.creator = ""           
        
        if self.category:
            self.categories = self.category.name
        else:
            self.categories = ""

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])
    
    def get_previous_by_updated_at(self):
        return self.objects.filter(yayimlanma_durumu='Yayinda',is_active=True,is_deleted=False, updated_at__lt=self.updated_at).order_by('-updated_at').first()
    
    def get_next_post(self):
        return self.get_next_by_updated_at()

    def get_previous_post(self):
        return self.get_previous_by_updated_at()