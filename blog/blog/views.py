from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag, Comment


def get_categories():
    all = Category.objects.all()
    count = all.count()
    return {"cat1": all[:count // 2], "cat2": all[count // 2:]}


def index(request):
    posts = Post.objects.all().order_by('-published_date')
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def about(request):
    context = {"posts": get_categories()}
    context.update(get_categories())
    return render(request, 'blog/about.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {"posts": get_categories(),
               "post": post}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def contact():
    return None


def category(request, slug):
    c = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {"posts": posts,}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def tag(request, slug):
    t = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tag=t).order_by('-published_date')
    context = {"posts": posts, }
    context.update(get_categories())
    return render(request, 'blog/index.html', context)
