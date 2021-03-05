from django.shortcuts import render

from webapp.models import Product, categories
# Create your views here

def list_product(request):
    lists = Product.objects.all()
    return render(request, 'list_product.html', context={'lists': lists})

def view_product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'view_product.html', context={'product': product})