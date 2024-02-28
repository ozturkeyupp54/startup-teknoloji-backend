# from rest_framework import serializers
# from category.models import Category
# from user.models import User
# # from comment.models import Comment
# from category.serializers import CategoryForPostSerializer
# from user.serializers import CreatorForPostSerializer
# from post.models import Post
# from comment.serializers import CommentSerializer


# class PostSerializer(serializers.ModelSerializer):

#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
#                                                   allow_null=True,
#                                                   required=False)
 
#     post_creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
#                                                   allow_null=True,
#                                                   required=False)

#     comments = serializers.SerializerMethodField()
#     post_views = serializers.SerializerMethodField()

#     class Meta:
#         model = Post
#         exclude = []
#         # fields = ['id',
#         #           'title',
#         #           'creator',
#         #           'slug',
#         #           'category',
#         #           'content',
#         #           'image',
#         #           'pub_date',
#         #           'status',
#         #           'post_views',
#         #           'comments',
#         #         #   'category_name',
#         #           # 'attachments',
#         #           'is_active',
#         #           'is_deleted',

#         #           ]

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['category'] = CategoryForPostSerializer(instance.category).data
#         representation['post_creator'] = CreatorForPostSerializer(instance.post_creator).data
#         return representation

#     def create(self, validated_data):
#         title = validated_data.get('title')
#         if not title:
#             raise serializers.ValidationError({"title": ["Bu alan Haber oluşturabilmeniz için gereklidir."]})
#         return super(PostSerializer, self).create(validated_data)

#     def get_comments(self, obj):
#         comments = obj.comment_set.all()
#         serializer = CommentSerializer(comments, many=True)
#         return serializer.data
    
#     def get_post_views(self,obj):
#         return obj.post_views
