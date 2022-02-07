from rest_framework import serializers
from .models import Post, Category, Tag


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pub_date_post = serializers.HiddenField(default=serializers.DateTimeField())
    pub_update = serializers.HiddenField(default=serializers.DateTimeField())

    class Meta:
        model = Post
        fields = '__all__'


class TagListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostListSerializers(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    tags = TagListSerializers(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tag
        fields = '__all__'


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = '__all__'
