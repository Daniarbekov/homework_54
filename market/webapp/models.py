from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100, null=False, blank=False)
    description = models.CharField(verbose_name='Описание', max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения',auto_now=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Описание',null=False, blank=False)
    category = models.ForeignKey( verbose_name='Категория',to='webapp.Category',related_name='category',null=False, blank=False, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Цена',null=False, blank=False, max_digits=10, decimal_places=3,)
    created_at = models.DateTimeField(verbose_name='Дата добавления',auto_now_add=True )
    image = models.CharField(verbose_name='Изображения',max_length=100,null=False, blank=False)
    changed_at = models.DateTimeField(verbose_name='Дата Изменения',auto_now=True)
