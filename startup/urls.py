from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from startup.sitemaps import PostSitemap
from homepage.views import HomeView, girisim_ve_yatirim, reklam_ve_sponsorluk,kariyer, kunye, iletisim


sitemaps = {
    'posts': PostSitemap,
    # Add other sitemaps here if you have more apps
}

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),  # Add this line for the root URL
    path('post/', include('post.urls'), name='post'),
    path('admin/', admin.site.urls),
    path('anket/', include('anket.urls'), name='anket'),
    path('user/', include('user.urls'), name='user'),
    path('author/', include('author.urls'), name='author'),
    path('auth/', include('authentication.urls'), name='authentication'),
    path('categories/', include('category.urls'), name='category'),
    path('investor/', include('investor.urls'), name='investor'),
    path('girisimci/', include('girisimci.urls'), name='girisimci'),
    path('girisim/', include('girisim.urls'), name='girisimci'),
    # path('entrepreneur/', include('entrepreneur.urls'), name='entrepreneur'),
    path('advertisement/', include('advertisement.urls'), name='advertisement'),
    path('alt_reklam_alani/', include('alt_reklam_alani.urls'), name='alt_reklam_alani'),
    path('comment/', include('comment.urls'), name='comment'),
    # path('django-check-seo/', include('django_check_seo.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('captcha/', include('captcha.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    
    path('girisim_ve_yatirim/', girisim_ve_yatirim, name='navbar-top/girisim_ve_yatirim'),
    path('reklam_ve_sponsorluk/', reklam_ve_sponsorluk, name='navbar-top/reklam_ve_sponsorluk'),
    # path('anket/', anket, name='navbar-top/anket'),
    path('kariyer/', kariyer, name='navbar-top/kariyer'),
    path('kunye/', kunye, name='navbar-top/kunye'),
    path('iletisim/', iletisim, name='navbar-top/iletisim'),
    
    
    # Serve static and media files during development
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': settings.DEBUG}),
]


