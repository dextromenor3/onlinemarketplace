from django.shortcuts import render

from .cart import Cart

def add_to_cart(request, item_id):
    cart = Cart(request)
