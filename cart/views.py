from django.shortcuts import render, redirect
from .cart import Cart
from ecomApp.models import Product


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('view_cart')


def view_cart(request):
    cart = Cart(request)
    product_ids = cart.cart.keys()
    product_ids_int = [int(pid) for pid in product_ids]
    products = Product.objects.filter(id__in=product_ids_int)
    item_count = len(product_ids_int)

    context = {'products': products, 'item_count': item_count}
    
    '''print("=== SESSION CART DATA ===")
    for product_id, item in cart.cart.items():
        print(f"Product ID: {product_id}, Quantity: {item['quantity']}")
    print("==========================")'''

    return render(request, 'cart.html', context=context)

