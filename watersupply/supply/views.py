from pyexpat.errors import messages
from urllib import request
from django.shortcuts import redirect, render
from .models import Company, Bottle
from django.contrib.auth import authenticate, login as auth_login
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
