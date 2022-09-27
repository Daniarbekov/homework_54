from django.contrib import admin
from webapp.models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields = ('id','description','name','created_at')
    list_display = ('id','description','name','created_at')
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','description','name','price','created_at')
    fields = ('id','description','name','price','created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)