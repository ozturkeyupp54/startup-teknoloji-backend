from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['yorum_birakanin_ismi', 'yorum_birakanin_eposta_adresi', 'content']

    def clean(self):
        cleaned_data = super().clean()

        # Gerekirse özel temizlik işlemleri ekleyebilirsiniz.

        return cleaned_data
