from .models import Category
from cart.cart import Cart

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

def cart_item_count(request):
    cart = Cart(request)
    items = cart.cart.keys()
    item_count = len(items)
    return {'item_count': item_count}
