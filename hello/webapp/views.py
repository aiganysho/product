from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Product, categories
from webapp.form import ProductForm
# Create your views here

def list_product(request):
    lists = Product.objects.all().exclude(remainder=0).order_by("category", "name")
    return render(request, 'list_product.html', context={'lists': lists})

def view_product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'view_product.html', context={'product': product})

def create_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create_product.html', {'category': categories, 'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data.get("name"),
                description=form.cleaned_data.get("description"),
                category=form.cleaned_data.get("category"),
                remainder=form.cleaned_data.get("remainder"),
                price=form.cleaned_data.get("price")
            )
            return redirect('view-product', pk=product.id)
        return render(request, 'create_product.html', context={'form': form})

def product_update_view(request, pk):

    product = get_object_or_404(Product, id=pk)

    if request.method == 'GET':
        form = ProductForm(
            initial={
                'name': product.name,
                'category': product.category,
                'description': product.description,
                'remainder': product.remainder,
                'price': product.price

            })
        return render(request, 'product_update.html',
                      context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(
            data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get("name")
            product.category = form.cleaned_data.get("category")
            product.description = form.cleaned_data.get("description")
            product.remainder = form.cleaned_data.get("remainder")
            product.price = form.cleaned_data.get("price")
            product.save()
            return redirect('view-product', pk=list.id)
        return render(request, 'product_update.html', context={'form': form, 'list': list})

def product_delete_view(request, pk):

    product = get_object_or_404(Product, id=pk)
    if request.method == "GET":
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('list-product')