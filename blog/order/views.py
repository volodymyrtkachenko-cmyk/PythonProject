from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart
from django.contrib import messages

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            messages.success(request, '')
            return render(request, 'order/order_create.html', {'order': order})
    else:
         form = OrderCreateForm()
    return render(request, 'order/order_create.html',{'form':form, 'cart':cart})