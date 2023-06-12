from rest_framework import serializers
from .models import Blog, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BlogListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'tags', 'thumbnail', 'created_at')


class BlogDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'tags', 'full_image', 'created_at')
