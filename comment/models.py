from django.db import models
from django.core.validators import MaxLengthValidator
from post.models import Post


class Comment(models.Model):
  
    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-pk']
        
    yorum_birakanin_ismi=models.CharField(max_length=80)
    yorum_birakanin_eposta_adresi=models.EmailField(max_length=80)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(limit_value=500)])
    target_to_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f"{self.yorum_birakanin_ismi}. {self.target_to_post}"

    def save(self, *args, **kwargs):
                # first_name ve last_name varsa, büyük harfe dönüştür
                if self.yorum_birakanin_ismi:
                    self.yorum_birakanin_ismi = self.yorum_birakanin_ismi.upper()

                super(Comment, self).save(*args, **kwargs)
