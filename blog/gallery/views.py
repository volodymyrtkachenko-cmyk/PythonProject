from django.contrib import messages
from django.shortcuts import render, redirect

from .models import GalleryImage
from .forms import GalleryImageForm


# Create your views here.
def gallery(request):
    images = GalleryImage.objects.all()
    context = {'images': images}
    return render(request, 'gallery/order_create.html', context)


def uploads(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryImageForm()
    return render(request, 'gallery/uploads.html', {'form': form})
