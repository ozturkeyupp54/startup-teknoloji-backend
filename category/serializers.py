from rest_framework import serializers

from post.models import Post
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    post_count = serializers.SerializerMethodField()
    breadcrumb = serializers.SerializerMethodField()
 

    class Meta:
        model = Category
        # exclude = []
        fields = [
            "id",
            "parent",
            "name",
            "slug",
            "breadcrumb",
            "children",
            "post_count",
            "is_active",
            "is_deleted",
            "created_at",
            "updated_at",
            "deleted_at", 
        ]
        read_only_fields = ["created_at", "updated_at", "deleted_at"]

    def get_children(self, obj):
        if obj.subcategories.all():
            return CategorySerializer(obj.subcategories.all(), many=True).data

    # Her bir kategorideki post sayısı:
    def get_post_count(self, obj):
        return Post.objects.filter(category=obj).count()

    """
    Oluşan kategori için "Breadcrumbs uzantısını veren listeyi" getirir. Meta class'daki isimle uyuşsun diye method
    adını da güncelledik. Böylece "breadcrumbs filed" her category için slugs'ları, ayrıca her "child category" 
    için "nested breadcrumbs"ları da geitirecektir.
    """

    def get_breadcrumb(self, obj):
        return obj.get_full_breadcrumb()


# ---------------------------------
# Extra Serializers
# ---------------------------------
# Kategoriye bağlı postları göster (related_name):
class CategoryForPostSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = [
            "id",
            "parent",
            "name",
            "slug",
            "post_count",
            "is_active",
            "is_deleted",
        ]
# Her bir kategorideki post sayısı:
    def get_post_count(self, obj):
        return Post.objects.filter(category=obj).count()
