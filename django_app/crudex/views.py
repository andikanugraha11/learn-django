from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm 

# Create your views here.


def getAllPruduct(request):
    products = Product.objects.all()

    context = {
        'products' : products 
    }

    return render(request,'index.html',context)

def addProduct(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        print(form)
        form.save()

        # URL
        return redirect('all_product')

    context = {
        'form'  : form
    }
    return render(request, 'product-form.html', context)

def updateProduct(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('all_product')

    context = {
        'form'      : form,
        'product'   : product
    }        
    return render(request, 'product-form.html', context)

def deleteProduct(request,id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('all_product')
    
    context = {
        'product'   : product
    } 
    return render(request,'prod-delete-confirm.html', context)
