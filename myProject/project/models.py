from django.db import models
from account.models import CustomUser 

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    category = models.CharField(max_length=100, verbose_name='Category')
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='menu', verbose_name='Image')
    discount=models.BooleanField(default=False, verbose_name='Discount')
    discountQuantityPrice = models.IntegerField(verbose_name='Discount Quantity Price', default=0)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    def save(self, *args, **kwargs):
        self.discountQuantityPrice = self.price - (self.price * 0.1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    surname = models.CharField(max_length=100, verbose_name='Surname')
    email = models.EmailField(max_length=100, verbose_name='Email')
    comment = models.TextField(verbose_name='Comment')
    customer_image = models.ImageField(upload_to='comment', verbose_name='Customer-image', default="")
    
    def __str__(self):
        return self.name

    
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Quantity', default=1)
    # price field will be calculated in views.py
    price = models.IntegerField(verbose_name='Price')
    
    def save(self, *args, **kwargs):
        self.price = self.quantity * self.menu.price
        super().save(*args, **kwargs)
  
    def __str__(self):
        return self.user.username
    
class Table(models.Model):
    tableNumber = models.IntegerField(primary_key=True, verbose_name='Table Number', default=1)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    
    def __str__(self):
        return 'Table ' + str(self.tableNumber)
  
class Rezervation(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='User',default=1)    
    name = models.CharField(max_length=100, verbose_name='Name')
    surname = models.CharField(max_length=100, verbose_name='Surname')
    email = models.EmailField(max_length=100, verbose_name='Email')
    phoneNumber = models.CharField(max_length=100, verbose_name='Phone Number')
    date = models.DateField(verbose_name='Date')
    time = models.TimeField(verbose_name='Time')
    people = models.IntegerField(verbose_name='People')
    table_number = models.ForeignKey(Table, verbose_name=("Table"), on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name  
    
    
