from django.shortcuts import render
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

def addProduct():
    form = ProductForm(request.POST or None)
    if form.is_valid():
        print(form)
        form.save()
        return redirect('getAllProduct')
    context = {
        'form'  : form
    }
    return render(request, 'product-form.html', context)

def updateProduct():
    pass