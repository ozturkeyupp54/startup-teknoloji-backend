from django.contrib import admin
from comment.models import Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # Number of empty attachment forms to display


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'target_to_post','is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ('content', 'target_to_post')

admin.site.register(Comment, CommentAdmin)
