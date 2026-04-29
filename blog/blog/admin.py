from django.contrib import admin

from .models import Post, Category, Tag, Comment, Subscribe, PostImage

admin.site.register(Comment)
admin.site.register(Subscribe)
admin.site.register(PostImage)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    autocomplete_fields = ('tag',)
    prepopulated_fields = {'slug': ('title',)}
