from django.urls import path
from webapp.views.index import index_view



urlpatterns= [
    path("", index_view, name='index'),
    path("products", index_view, name='products')
]