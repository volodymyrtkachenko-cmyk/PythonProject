from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now

from .forms import PostForm, CommentForm, SubscribeForm
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.published_date = now()
            comment.post = Post.objects.get(slug=slug)
            comment.user = request.user
            comment.save()
            messages.success(request, "Коментар додано!")
            return redirect('index')
    else:
        form = CommentForm()
    post = get_object_or_404(Post, slug=slug)
    context = {"posts": get_categories(),
               "post": post,
               "form": form}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def contact(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            new_subscribe = form.save(commit=False)
            new_subscribe.save()
            messages.success(request, 'Підписка оформлена')
            return redirect('index')
    else:
        form = SubscribeForm()
    context = {"form": form}
    context.update(get_categories())
    return render(request, 'blog/contact.html', context)


def category(request, slug):
    c = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {"posts": posts, }
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def tag(request, slug):
    t = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tag=t).order_by('-published_date')
    context = {"posts": posts, }
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query)).order_by('-published_date')
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published_date = now()
            new_post.save()
            form.save_m2m()
            messages.success(request, 'Пост додано успішно!')
            return redirect('index')
    else:
        form = PostForm()
    context = {"form": form}
    context.update(get_categories())
    return render(request, 'blog/create_post.html', context)



