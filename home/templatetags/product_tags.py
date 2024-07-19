from django import template
from order.models import *
register = template.Library()

@register.simple_tag
def call_sellprice(price,discount):
    if discount is None or discount is 0:
        return price
    sellprice = price
    sellprice = price - (price* discount/100)
    return sellprice

@register.simple_tag
def multiply(price,qty):
    total = price * qty
    return total

@register.simple_tag
def total_amount(cid):
    c = Cart.objects.filter(customer_id=cid)
    t=0
    if c:
        for c in c:
            price = c.product.price
            dic = c.product.discount
            qty = c.qty
            sellprice = price - (price* dic/100)
            total = sellprice * qty
            t += total
    return t
