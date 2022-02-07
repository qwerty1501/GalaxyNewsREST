from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', db_index=True, max_length=50)
    content = models.TextField('Описание', blank=True, null=True)
    pub_date_post = models.DateTimeField('Дата публикации', auto_now_add=True)
    pub_update = models.DateTimeField('Дата обновления', auto_now=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    tags = models.ManyToManyField('Tag', blank=True, related_name='tag_posts')
    categories = models.ForeignKey('Category', on_delete=models.PROTECT)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date_post']


class Tag(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"
