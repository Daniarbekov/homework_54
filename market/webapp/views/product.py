
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product, Category


def product_add_view(request):
    if request.method == 'GET':
        context = {
            'categories' : Category.objects.all()
        }
        print(context)
        return render(request, 'add_product.html', context)
    product_data = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image'),
        'category': Category.objects.get(name=request.POST.get('category'))
    }
    product = Product.objects.create(**product_data)
    return redirect("/")


def product_view(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail_product.html', context={'product': product})

def product_delete(request,pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('/')

def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_edit.html', context={'product': product,'categories' : Category.objects.all()})
    else:
        product.name = request.POST.get('name')
        product.image = request.POST.get('image')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.category = Category.objects.get(name=request.POST.get('category'))
        product.save()
        return redirect('product_detail',pk=product.pk)