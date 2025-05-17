from django.shortcuts import render, redirect
from .cart import Cart
from ecomApp.models import Product
from django.contrib.auth.decorators import login_required


# add the products to the shoping cart
@login_required(login_url='login')
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
@login_required(login_url='login')
def view_cart(request):
    cart = Cart(request)
    products = cart.get_products()
    cart_total = cart.cart_total()
   
    context = {'products': products, 'cart': cart, 'cart_total': cart_total}
    
    return render(request, 'cart.html', context=context)

# updating the shoping cart
@login_required(login_url='login')
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
@login_required(login_url='login')
def delete_item(request, product_id):
    cart = Cart(request)
    cart.delete(product_id)
    return redirect('view_cart')