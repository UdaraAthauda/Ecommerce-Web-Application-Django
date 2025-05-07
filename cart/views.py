from django.shortcuts import render, redirect
from .cart import Cart
from ecomApp.models import Product


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('view_cart')


def view_cart(request):
    cart = Cart(request)
    products = cart.get_products
   
    context = {'products': products}
    
    '''print("=== SESSION CART DATA ===")
    for product_id, item in cart.cart.items():
        print(f"Product ID: {product_id}, Quantity: {item['quantity']}")
    print("==========================")'''

    return render(request, 'cart.html', context=context)

