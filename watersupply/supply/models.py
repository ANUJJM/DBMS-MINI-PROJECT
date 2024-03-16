from django.db import models

# Create your models here.

class Bottle(models.Model):
    bottleid = models.AutoField(primary_key=True)
    brandname = models.CharField(max_length=45)
    size = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    bottledetailscol = models.CharField(max_length=45)

class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)


class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    phonenumber = models.BigIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userid', 'phonenumber'], name='user_primary_key')
        ]


class Company(models.Model):
    companyid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    contactnum = models.CharField(max_length=45)
    email = models.EmailField()


class OrderAddress(models.Model):
    ordaddid = models.IntegerField(primary_key=True)
    orderid = models.IntegerField()
    addressline = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)



class Order(models.Model):
    orderid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    orddate = models.CharField(max_length=45)
    deliverydate = models.CharField(max_length=45)
    status = models.CharField(max_length=45)


class OrderAddress(models.Model):
    ordaddid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    orderaddcol = models.CharField(max_length=45)



class Bottle(models.Model):
    bottleid = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.CharField(max_length=45)
    stock = models.CharField(max_length=45)



class UserDetails(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=45)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
User.cart = property(lambda u: Cart.objects.get_or_create(user=u)[0])
