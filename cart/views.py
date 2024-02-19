from django.shortcuts import render
from django.template import RequestContext 
from cart import cart 

# Create your views here.
def show_cart(request, template_name="cart/cart.html"):
    cart_items = cart.get_cart_items(request)
    cart_item_count = cart.cart_item_count(request)
    page_title = 'Shopping Cart'
    cart_subtotal = 0
    for cart_item in cart_items:
        cart_subtotal += cart_item.quantity * cart_item.product.price
    return render(request, template_name, locals())

