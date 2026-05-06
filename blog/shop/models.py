import os
from PIL import Image
from django.db import models
from slugify import slugify
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="назва")
    slug = models.SlugField(max_length=120, blank=True, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категорія"
        verbose_name_plural = 'категорії'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(verbose_name="опис")
    image = models.ImageField(upload_to='shop/')
    thumbnail = models.ImageField(upload_to='shop/thumbnail/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)
    published_date = models.DateTimeField(default=timezone.now, verbose_name="дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='products')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

        if self.image and not self.thumbnail:
            self.create_thumbnail()
            super().save(update_fields=['thumbnail'])

    def create_thumbnail(self):
        if not self.image:
            return

        img_path = self.image.path
        img = Image.open(img_path)
        img.thumbnail((200, 200))

        thumb_name = os.path.basename(img_path)
        thumb_relative_path = os.path.join('shop', 'thumbnail', thumb_name)
        thumb_full_path = os.path.join(os.path.dirname(img_path), 'thumbnail', thumb_name)

        os.makedirs(os.path.dirname(thumb_full_path), exist_ok=True)
        img.save(thumb_full_path)

        self.thumbnail = thumb_relative_path


class Product_image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', blank=True)
