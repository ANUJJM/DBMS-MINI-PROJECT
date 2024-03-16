from pyexpat.errors import messages
from urllib import request
from django.shortcuts import redirect, render
from .models import Company, Bottle
from django.contrib.auth import authenticate, login as auth_login
from .models import Product, Cart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})

def company_products(request, company_id):
    company = Company.objects.get(pk=company_id)
    products = Bottle.objects.filter(company=company)
    return render(request, 'company_products.html', {'company': company, 'products': products})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def checkout(request):
    return render(request,'checkout.html')

def login_view(request):
     from django.contrib import messages

def myaccount(request):
    return render(request,'myaccount.html')

def myorder(request):
    return render(request,'myorder.html')

def login_view(request):
    if request.method == 'POST':
        # Retrieve username and password from the form submission
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log in the user and redirect to a success page
            auth_login(request, user)  # Use the renamed login function
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # If authentication fails, add an error message
            messages.error(request, 'Invalid username or password')

    # If the request method is not POST (e.g., GET), render the login page template
    return render(request, 'login.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('product-list')

@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart.objects.get(user=request.user)
    try:
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity >= 1:
             cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    
    return redirect('cart')


@login_required(login_url='login')
def view_cart(request):
    cart = request.user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required(login_url='login')
def increase_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

@login_required(login_url='login')
def decrease_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.get(product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


@login_required(login_url='login')
def fetch_cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = request.user.cart
        cart_count = CartItem.objects.filter(cart=cart).count()
    return JsonResponse({'cart_count': cart_count})

def get_cart_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart=request.user.cart)
        cart_count = cart_items.count()
    else:
        cart_count = 0
    return cart_count
