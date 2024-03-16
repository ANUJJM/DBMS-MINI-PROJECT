from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    # path('cart', views.cart, name='cart'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('company/<int:company_id>/', views.company_products, name='company_products'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('checkout/', views.checkout, name='checkout'),
    path('myorder', views.myorder, name='myorder'),
    # added
    path('product-list/', product_list, name='product-list'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('cart/', view_cart, name='cart'),
    path('increase-cart-item/<int:product_id>/', increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<int:product_id>/', decrease_cart_item, name='decrease-cart-item'),
    path('fetch-cart-count/', fetch_cart_count, name='fetch-cart-count')
      # Ensure the name is 'company_products'
    # Example pattern
    # Add more URL patterns here as needed
]
