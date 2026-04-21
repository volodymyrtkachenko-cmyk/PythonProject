from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="назва")
    slug = models.SlugField(max_length=120, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категорія"
        verbose_name_plural = 'категорії'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=15, verbose_name="назва")
    slug = models.SlugField(max_length=120, unique=True, blank=True, )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="заголовок")
    content = models.TextField(verbose_name="опис")
    slug = models.SlugField(max_length=220, blank=True, unique=True)
    published_date = models.DateTimeField(default=timezone.now, verbose_name="дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор")
    tag = models.ManyToManyField(Tag, verbose_name="тег", blank=True)
    image = models.URLField(default='https://img.freepik.com/free-vector/user-blue-gradient_78370-4692.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новина"
        verbose_name_plural = 'новини'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField(default='', max_length=100, verbose_name='опис')
    published_date = models.DateTimeField(default=timezone.now, verbose_name="дата публікації")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост', related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="автор", blank=True, null=True )

    def __str__(self):
        return f"{self.post.title}"

    class Meta:
        verbose_name = "коментар"
        verbose_name_plural = 'коментарі'


class Subscribe(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='імʼя')
    email = models.EmailField(verbose_name='пошта')

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = "підписка"
        verbose_name_plural = 'підписки'