from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
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


@login_required
def delete_product(request, pk):
    if not request.user.is_staff:
        return HttpResponse('YOU ARE Not allowed to delete books')
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('products:products')

def orders(request,id):
    product=Product.objects.filter(id=id)
    return render(request,'orders.html',{'product':product})


           
def single_product(request,id):
    product=Product.objects.filter(id=id)
    return render(request,'single-product.html',{'product':product})

def home(request):
     product_list = Product.objects.all()
     context = {
        'product_list': product_list,
    }
     return render(request,'product.html',context)

def charts(request):
    big = products.objects.filter(type=products.ProductType.BIG_ITEM).count()
    small = products.objects.filter(type==products.ProductType.SMALL_ITEM).count()
    return render(request, "charts.html", {"big":big, "small":small})

def buy_product(request):
    cart = request.GET
    product = Product.objects.all
    return render(request,"cart.html",{'cart':cart})

# def add_to_cart(request,product_id):
#     if request.user.is_authenticated():
#         try:
#             product = Product.objects.get(pk=product_id)
#         else :
#             try:
#                 cart = Cart.objects.get(user = request.user, active = True)
#             except ObjectDoesNotExist:
#                 cart = Cart.objects.create(user = request.user)
#                 cart.save()
#                 cart.add_to_cart(product_id)
#                 return redirect('cart')
#             else:
#                 return redirect('index')


# def remove_from_cart(request, product_id):
#     if request.user.is_authenticated():
#         try:
#             cart = Cart.objects.get(pk = product_id)
#         except ObjectDoesNotExist:
#             pass 
#         else:
#             cart = Cart.objects.get(user = request.user, active = True)
#             cart.remove_from_cart(product_id)
#         return redirect('cart')
#     else:
#         return redirect('index')