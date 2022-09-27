
from unicodedata import category
from django.shortcuts import render, redirect
from webapp.models import Category


def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'add_category.html')
    category = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
    }
    category = Category.objects.create(**category)
    return redirect("/")