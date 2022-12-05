from django.db import models

# Create your models here.
from enum import Enum
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductType(Enum):
    BIG_ITEM = 1
    SMALL_ITEM = 2
 
class Product(models.Model):   
    class ProductType2(models.IntegerChoices):
        BIG_ITEM = 1, "bigger then 10 inch"
        SMALL_ITEM = 2, "smaller then 10 inch"      

    name = models.CharField(max_length=200, null=False)
    seller = models.CharField(max_length=200, null=False)
    Year_manufacture = models.DateField()
    type = models.SmallIntegerField(choices=ProductType2.choices, default=ProductType2.BIG_ITEM , null=False)
    price = models.DecimalField(decimal_places=2,max_digits=100 ,default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    def __str__(self):
        return self.name

class Buy(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    buy_date = models.DateTimeField()
    price = models.DecimalField(decimal_places=2,max_digits=100 ,default=True)

# class Cart(models.Model):
#     user = models.ForeignKey(User)
#     active = models.BooleanField(default=True)
#     order_date = models.DateField(null=True)
#     payment_type = models.CharField(max_length=100, null=True)
#     payment_id = models.CharField(max_length=100, null=True)

#     def __unicode__(self): 
#             return "%s" % (self.user)

#     def add_to_cart(self, book_id):
#         book = Book.objects.get(pk=book_id)
#         try:
#             preexisting_order = BookOrder.objects.get(book=book, cart=self)
#             preexisting_order.quantity += 1
#             preexisting_order.save()
#         except BookOrder.DoesNotExist:
#             new_order = BookOrder.objects.create(
#                 book=book,
#                 cart=self,
#                 quantity=1
#                 )
#             new_order.save()

#             def __unicode__(self):
#                 return "%s" % (self.book_id)


#     def remove_from_cart(self, book_id):
#         book = Book.objects.get(pk=book_id)
#         try:
#             preexisting_order = ProductsOrder.objects.get(book=book, cart=self)
#             if preexisting_order.quantity > 1:
#                 preexisting_order.quantity -= 1
#                 preexisting_order.save()
#             else:
#                 preexisting_order.delete()
#         except BookOrder.DoesNotExist:
#             pass