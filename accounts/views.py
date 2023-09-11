from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.contrib import messages, auth
from cart.views import _cart_id
from cart.models import Cart, CartItem
from django.contrib.auth import login,logout,authenticate


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cart')
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    return render(request, 'accounts/dashboard.html')

def signin(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    for item in cart_item:
                        item.user = user
                        item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('signin')
    return render(request, 'accounts/signin.html')


def user_logout(request):
    logout(request)
    return redirect('signin')
