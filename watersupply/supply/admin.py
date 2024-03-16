from django.contrib import admin
from .models import Bottle,Order,User,Company,OrderAddress,UserDetails
from .models import Profile, Product, Cart, CartItem

# Register your models here.
admin.site.register(Bottle)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Company)
admin.site.register(OrderAddress)
admin.site.register(UserDetails)

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
