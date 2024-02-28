from django.contrib.sitemaps import Sitemap
from post.models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(is_active = True) 

    def lastmod(self, obj):
        return obj.updated_at



