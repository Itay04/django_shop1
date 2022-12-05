from django.contrib import admin

from products.models import Buy, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Buy)
