from django.urls import path
from webapp.views.index import index_view
from webapp.views.category import category_add_view
from webapp.views.product import product_add_view, product_view, product_delete, product_update_view



urlpatterns= [
    path("", index_view, name='index'),
    path("products", index_view, name='products'),
    path("categories/add", category_add_view, name='category_add'),
    path("products/add", product_add_view, name='product_add'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('products/<int:pk>/delete', product_delete, name='product_delete'),
    path('products/<int:pk>/edit', product_update_view, name='product_update')
]