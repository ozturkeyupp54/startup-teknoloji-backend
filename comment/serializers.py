from rest_framework import serializers
# from post.models import Post
from comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    # post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(),
    #                                              allow_null=True,
    #                                              required=False)

    class Meta:
        model = Comment
        exclude = []
        # fields = ['id',
        #           'user',
        #           'content',
        #           # 'post',
        #           'target_to_post',
        #           'time_stamp',
        #           'is_active',
        #           'is_deleted',
        #           ]

    def create(self, validated_data):
        content = validated_data.get('content')
        if not content:
            raise serializers.ValidationError({"content": ["Bu alan yorum oluşturabilmeniz için gereklidir."]})
        return super(CommentSerializer, self).create(validated_data)


# class CommentForPostSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = ['id',
#                   'content',
#                   ]
