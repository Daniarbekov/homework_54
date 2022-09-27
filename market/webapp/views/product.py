
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
