from rest_framework import generics, viewsets
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import Post, Tag, Category
from .permissions import *
from rest_framework.permissions import IsAuthenticated


class NewsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializers
    queryset = Post.objects.all()


class PostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class TagCreateView(generics.CreateAPIView):
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)


class TagListView(generics.ListAPIView):
    serializer_class = TagListSerializers
    queryset = Tag.objects.all()


class TagUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializers
    queryset = Category.objects.all()


class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class ImageViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put']
    queryset = Post.objects.all()