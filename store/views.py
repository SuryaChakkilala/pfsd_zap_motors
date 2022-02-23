from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.contrib import messages
from .forms import CreateUserForm
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('store')
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account was created for {form.cleaned_data.get("username")}')
            email = EmailMessage(
                'Welcome to Zap Motors!',
                'Thank you for registering your account on Zap Motors',
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
            )
            email.fail_silently = False
            email.send()
            return redirect('login')
            
    context = {'form': form}
    return render(request, 'store/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('store')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'Username (or) Password is incorrect!')
    context = {}
    return render(request, 'store/login.html', context)

def logoutPage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('login')

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def car_view(request, car_name):
    product = Product.objects.get(name=car_name)
    context = {'product': product}
    return render(request, 'store/vehicle_page.html', context)

def checkout(request, product_name):
    if not request.user.is_authenticated:
        return redirect('login')

    product = Product.objects.get(name=product_name)
    if request.method == "POST":
        product_name = product.name
        user = request.user
        order = Order(user=request.user, product_name=product_name)
        order.save()
        return redirect('success', product_name=product_name)
    context = {'product': product}
    return render(request, 'store/checkout.html', context=context)

def success(request, product_name):
    if not request.user.is_authenticated:
        return redirect('login')
    product = Product.objects.get(name=product_name)
    context = {'product': product, 'customer': request.user.username}
    return render(request, 'store/payment_success.html', context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.all().filter(user=request.user.username)
    context = {'orders': orders}
    return render(request, 'store/profile.html', context)