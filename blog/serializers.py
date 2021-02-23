from rest_framework import serializers

from .models import Blog, Tag


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "pk",
            "title",
            "slug",
            "user",
            "created_at",
            "updated_at",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "pk",
            "name",
            "blog",
        )
