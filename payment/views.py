from django.shortcuts import render
from cart.cart import Cart


# checkout view
def checkout(request):
    cart = Cart(request)
    products = cart.get_products()
    cart_total = cart.cart_total()
   
    context = {'products': products, 'cart': cart, 'cart_total': cart_total}
    
    return render(request, 'checkout.html', context=context)

