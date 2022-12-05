from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from products.forms import ProductForm
from products.models import Product


def products(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'product.html', context)

def add_product(request):
    context = {
        'productform': ProductForm(),
    }
    return render(request, 'addproduct.html', context)

def add_product_action(request):
    productform = ProductForm(request.POST, request.FILES)
    if productform.is_valid():
        productform.save()
        return redirect('products:products')
    else:
        context = {
            'productform': productform,
        }
        return render(request, 'addproduct.html', context)

def find_product(request):
    return HttpResponse("PRODUCT FOUND")


def delete_product(request):
    return HttpResponse("product DELETED")

def buy_product(request):
    buy=request.GET
    product=Product.objects.all
    return render(request,"buy.html",{'buy':buy})


            
def single_product(request,id):
    product=Product.objects.filter(id=id)
    return render(request,'single-product.html',{'product':product})

def home(request):
     product_list = Product.objects.all()
     context = {
        'product_list': product_list,
    }
     return render(request,'index.html',context)

def charts(request):
    big = products.objects.filter(type=products.ProductType.BIG_ITEM).count()
    small = products.objects.filter(type==products.ProductType.SMALL_ITEM).count()
    return render(request, "charts.html", {"big":big, "small":small})
