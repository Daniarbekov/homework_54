from django.urls import path
from webapp.views.index import index_view
from webapp.views.category import category_add_view
from webapp.views.product import product_add_view



urlpatterns= [
    path("", index_view, name='index'),
    path("products", index_view, name='products'),
    path("categories/add", category_add_view, name='category_add'),
    path("products/add", product_add_view, name='product_add')
]