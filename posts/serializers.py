from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    comments = serializers.SlugRelatedField(
        many=True, slug_field="content", read_only=True
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "post_title",
            "link",
            "created_at",
            "upvotes_counter",
            "author",
            "comments",
        )
        read_only_fields = ("upvotes_counter",)
