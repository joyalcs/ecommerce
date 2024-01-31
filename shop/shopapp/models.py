from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self) -> str:
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('shopapp:cat_products', args=[self.slug])


class Product(models.Model):
    name= models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self) -> str:
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('shopapp:product', args=[self.category.slug, self.slug])
