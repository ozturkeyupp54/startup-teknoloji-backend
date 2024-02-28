from django.contrib import admin
from user.models import User

class UserAdmin(admin.ModelAdmin):
    # exclude = ('password', 'login_attemp')
    list_display = ('full_name','username', 'email', 'is_staff')
    list_filter = ('is_active', 'is_deleted')
    list_display_links = ['username', 'full_name']
    search_fields = ('full_name', 'email')

admin.site.register(User,UserAdmin)

