from django.shortcuts import render, redirect
from cart.cart import Cart
from ecomApp.models import User
from .models import *
from ecomApp.models import Product



# checkout view
def checkout(request):
    cart = Cart(request)
    products = cart.get_products()
    cart_total = cart.cart_total()
    shipping_detail = User.objects.get(id=request.user.id)
   
    context = {'products': products, 'cart': cart, 'cart_total': cart_total, 'shipping_detail': shipping_detail}
    
    return render(request, 'checkout.html', context=context)

# order process view
def process_order(request):
    shipping_detail = User.objects.get(id=request.user.id)
    cart = Cart(request)

    # gather order info
    user = request.user
    full_name = f'{shipping_detail.first_name} {shipping_detail.last_name}'
    email = shipping_detail.email
    shipping_address = shipping_detail.address
    amount_paid = cart.cart_total()

    # create an order
    if user:
        create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
        create_order.save()

        # create order items
        order_id = create_order.pk

        for product in cart.get_products():
            product_id = product.id

            # get the product price
            if product.is_sale:
                price = product.sale_price
            else:
                price = product.price

            # get the product quantity
            for key, value in cart.cart.items():
                if int(key) == product.id:
                    quantity = value.get('quantity')

                    create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=quantity, price=price)
                    create_order_item.save()

        # delete the ordered cart
        for key in list(request.session.keys()):
            if key == "cart":
                del request.session[key]

    return redirect('home')

# get user orders for review
def orders(request):
    user_orders = Order.objects.filter(user=request.user)
    order_items = OrderItem.objects.filter(order__in=user_orders)

    context = {'user_orders': user_orders, 'order_items': order_items}

    return render(request, 'orders.html', context=context)