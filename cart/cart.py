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

    # add products ids to the session cart 
    def add(self, product_id, quantity=1):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity}
        self.save()

    # updating cart
    def update(self, product_id, quantity):
        product_id = str(product_id)
        quantity = int(quantity)

        cart = self.cart

        cart[product_id] = {'quantity': quantity}

        self.save()

    # delete products from the shoping cart
    def delete(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.save()

    def save(self):
        self.session.modified = True
    
    # retrieve the product ids from cart and filter the products from database
    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    # shoping cart total price calculation
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        quantitys = self.cart
        total = 0

        for key, value in quantitys.items():
            key = int(key)
            quantity = value.get('quantity')
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * quantity)
                    else:
                        total = total + (product.price * quantity)    
        
        return total

