from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Product_image

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


def category_view(request, slug):
    p = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=p).order_by('-published_date')
    context = {'products': products}
    return render(request, 'shop/index.html', context)


def product_view(request, slug):
    product = Product.objects.get(slug=slug)
    images = Product_image.objects.filter(product=product)
    return render(request, 'shop/product.html', {'product': product, 'images': images})