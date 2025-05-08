from django.shortcuts import render, redirect
from .cart import Cart
from ecomApp.models import Product


# add the products to the shoping cart
def add_to_cart(request):
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        # Validate input
        if product_id and quantity:
            try:
                quantity = int(quantity)
                cart = Cart(request)
                cart.add(product_id, quantity)
            except ValueError:
                pass

    return redirect('view_cart')

# view the products added to the shoping cart
def view_cart(request):
    cart = Cart(request)
    products = cart.get_products()
   
    context = {'products': products, 'cart': cart}
    
    return render(request, 'cart.html', context=context)

# updating the shoping cart
def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        # Validate input
        if product_id and quantity:
            try:
                quantity = int(quantity)
                cart = Cart(request)
                cart.update(product_id, quantity)
            except ValueError:
                pass
    
    return redirect('view_cart')

# delete item from the shoping cart
def delete_item(request, product_id):
    cart = Cart(request)
    cart.delete(product_id)
    return redirect('view_cart')