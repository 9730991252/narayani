from django import template
from order.models import *
register = template.Library()

@register.simple_tag
def multiply(price,qty,n):
    cr = n * qty
    total = price * qty + cr
    return total


@register.simple_tag
def cart_courier_charges(pid,cid,qty,):
    c = Customer.objects.get(id=cid)
    if c.state == '1':
        p = Product.objects.filter(id=pid)
        if p:
            for p in  p:
               cu = p.courier_charges_maharashtra
               return cu
    if c.state == '0':
        p = Product.objects.filter(id=pid)
        if p:
            for p in  p:
               cu = p.courier_charges_other_states
               return cu


@register.simple_tag
def total_amount(cid):
    cus = Customer.objects.get(id=cid)
    c = Cart.objects.filter(customer_id=cid)
    total = 0
    if c:
        for c in c:
            pid = c.product_id
            price = c.product.price 
            qty = c.qty
            tprice = qty * price
            cur =  qty * (c.product.courier_charges_maharashtra if cus.state == '1' else c.product.courier_charges_other_states) 
            total += tprice + cur

    return total