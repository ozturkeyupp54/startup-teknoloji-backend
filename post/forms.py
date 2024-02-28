from django import forms
from post.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'categories', 'content', 'haber_baslik_resmi', 'link', 'yayimlanma_durumu']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'ckeditor'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Haberin başlık alanı mutlaka eklenmelidir.")
        return title
