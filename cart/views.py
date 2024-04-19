from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.http import JsonResponse
from app.models import Product


def CartView(request):
    return render(request, 'Product_Cart.html')


def AddCart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, product_id=product_id)
        cart.add(product=product)
        response = JsonResponse({'name': product.name})
        return response
