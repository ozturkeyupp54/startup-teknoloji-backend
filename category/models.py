from django.db import models
from utils.utils import turkish_slugify

class Category(models.Model):
    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['pk']

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig_queryset = Category.objects.filter(pk=self.pk)
            if orig_queryset.exists():
                orig = orig_queryset.first()
                if orig.slug != self.slug:
                    self.slug = turkish_slugify(self.name)
        else:
            self.slug = turkish_slugify(self.name)

        super(Category, self).save(*args, **kwargs)


