from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'З поверненням!')
            return redirect('index')
        else:
            messages.error(request, 'Не вірний логін або пароль!')
    return render(request, 'accounts/login.html')





@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Дякуємо що були з нами!')
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(Q(username__icontains=username) | Q(email__icontains=email)).exists():
            messages.error(request, 'Аккаунт з таким email або імʼям вже існує!')
            return render(request, 'accounts/register.html')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request,'Реєстрація успішна!')
            return redirect('index')
    return render(request, 'accounts/register.html')






