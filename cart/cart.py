from ecomApp.models import Product

class Cart():
    
    def __init__(self, request):
        self.session = request.session

        # get the current session key if it exists
        cart = self.session.get('cart')

        # if no session key, create one
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product_id, quantity=1):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity}
        self.save()

    def save(self):
        self.session.modified = True
    
    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products