from django.forms import ModelForm
from .models import Product
from django.contrib.auth.models import User

 
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'seller', 'Year_manufacture', 'type', 'image']
 
        