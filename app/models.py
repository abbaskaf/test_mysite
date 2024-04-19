from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    Discount_choices = [
        ('Activ', 'activ'),
        ('Inactive', 'inactive')
    ]

    title = models.CharField(max_length=20, null=False, blank=False)
    active = models.CharField(max_length=8, choices=Discount_choices)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categorys')
        ordering = ['id']

    def __str__(self):
        return self.title


class Product(models.Model):
    IsDiscount = [
        ('Discount', 'discount'),
        ('Nodiscount', 'nodiscount')
    ]

    class Publish(models.TextChoices):
        Publish = 'Publish', 'publish'
        Nopublish = 'Nopublish', 'nopublish'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='name')
    brand = models.CharField(max_length=20, verbose_name='Brand')
    property = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Price')
    publish = models.CharField(max_length=9, choices=Publish.choices, default=Publish.Nopublish)
    is_discount = models.CharField(max_length=10, choices=IsDiscount, default='Nodiscount')
    discount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Discount')
    at_create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    score = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['id']

    def __str__(self):
        return f'{self.category}|{self.name}'


class Image(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='photo/')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

