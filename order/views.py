from django.shortcuts import render,redirect
from order.models import *
from django.db.models import Sum
# Create your views here.
def cart(request):
    context={}
    if request.session.has_key('customer_mobile'):
        customer_mobile=request.session['customer_mobile']
        cm=Customer.objects.get(mobile=customer_mobile)
        cp=Cart.objects.filter(customer_id=cm.id)
        if 'Remove' in request.GET:
            cart_id=request.GET.get('cart_id')
            if Cart.objects.filter(id=cart_id).first():
                Cart.objects.get(id=cart_id).delete()
                if len(Cart.objects.filter(customer_id=cm.id)) == 0:
                    return redirect('/')

        if 'Add_address' in request.POST:
            name=request.POST.get('name')
            pin_code=request.POST.get('pin_code')
            house_no=request.POST.get('house_no')
            post=request.POST.get('post')
            taluka=request.POST.get('taluka')
            district=request.POST.get('district')
            landmark=request.POST.get('landmark')
            state_name=request.POST.get('state_name')
            Customer(
                id=cm.id,
                mobile=cm.mobile,
                date=cm.date,
                name=name,
                pin_code=pin_code,
                house_no=house_no,
                post=post,
                taluka=taluka,
                district=district,
                landmark=landmark,
                state_name=state_name,
            ).save()
            total_amount=0
            f=OrderMaster.objects.all().count()
            f+=1
            if cp:
                for c in cp:
                    pid=c.product_id
                    qty=c.qty
                    curent_p=Product.objects.filter(id=pid)
                    if curent_p:
                        for curent_p in curent_p:
                            price=curent_p.price
                            total=price*qty
                            courier_charges = qty * (curent_p.courier_charges_maharashtra if cm.state == '1' else curent_p.courier_charges_other_states)
                            total_amount+= total + courier_charges
            OrderMaster(
                customer_id=cm.id,
                total_amount=total_amount,
                order_filter=f,
            ).save()
            total_amount_d=0
            if cp:
                for cd in cp:
                    pid_d=cd.product_id
                    qty_d=cd.qty
                    curent_p_d=Product.objects.filter(id=pid_d)
                    if curent_p_d:
                        for curent_p_d in curent_p_d:
                            price_d=curent_p_d.price
                            total_d=price_d*qty_d
                            courire_total = qty_d * (curent_p_d.courier_charges_maharashtra if cm.state == '1' else curent_p_d.courier_charges_other_states)
                            total_amount_d = total_d + courire_total
                            Order_detail(
                                customer_id=cm.id,
                                product_id=pid_d,
                                product_name=curent_p_d.product_name,
                                price=curent_p_d.price,
                                qty=qty_d,
                                courier_charges=(curent_p_d.courier_charges_maharashtra if cm.state == '1' else curent_p_d.courier_charges_other_states) ,
                                total_price=total_amount_d,
                                order_filter=f,
                            ).save() 
                cp=Cart.objects.filter(customer_id=cm.id).delete()
                return redirect('/')
        context={
            'cp':cp,
            'cm':cm,
            }
        return render (request,'order/cart.html',context)

    else:
        return redirect('/')
    
#order
def order(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        return render(request, 'order/order.html')
    else:
        return redirect('/login/')
    
def pending_order(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}

        context={
            'om':OrderMaster.objects.filter(status='Pending').order_by('-id')
        }
        return render(request, 'order/pending_order.html',context)
    else:
        return redirect('/login/')
    

def view_pending_order(request,order_filter):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        o = Order_detail.objects.filter(order_filter=order_filter)
        ord = Order_detail.objects.filter(order_filter=order_filter).first()
        c = Customer.objects.get(id=ord.customer_id)
        total_amount = Order_detail.objects.filter(order_filter=order_filter,stock_status=1).aggregate(Sum ('total_price'))
        total_amount = total_amount['total_price__sum']
        if total_amount is None:
            total_amount = 0.0
        context={
            'o':o,
            'c':c,
            'ord':ord,
            'total_amount':total_amount,
        }
        return render(request, 'order/view_pending_order.html',context)
    else:
        return redirect('/login/')
    
















