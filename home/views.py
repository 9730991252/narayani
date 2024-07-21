from django.shortcuts import render , redirect 
from django.contrib import messages 
from product.models import *
from order.models import *
from customer.models import *
# Create your views here.
def index(request):
    #Product.objects.all().delete()
    #Cart.objects.all().delete()
    #Customer.objects.all().delete()
    #Order_detail.objects.all().delete()
    #OrderMaster.objects.all().delete()
    #del request.session['customer_mobile']
    ng=0
    if request.session.has_key('customer_mobile'):
        customer_mobile = request.session['customer_mobile']
        cm=Customer.objects.filter(mobile=customer_mobile).first()
        if cm:
            cm=Customer.objects.get(mobile=customer_mobile)
            ng=len(Cart.objects.filter(customer_id=cm.id))
        else:
            del request.session['customer_mobile']
    context={
        'c':Category.objects.all(),
        'ng':ng,
    }
    return render(request, 'home/index.html',context)

def login(request):
    if request.session.has_key('owner_mobile'):
        return redirect('/owner/owner_dashboard/')
    if 'Login' in request.POST:
        num = request.POST.get('number')
        pin = request.POST.get('pin')
        owner_login={'mobile':'123','pin':'123'}
        if owner_login["mobile"]==num and owner_login["pin"]==pin:
            request.session['owner_mobile'] = request.POST.get('number')
            return redirect('/owner/owner_dashboard/')
        else:
            messages.warning(request,"please insert correct information or call more suport 9921856831")
    return render(request, 'home/login.html' )

def logout (request):
    del request.session['owner_mobile']
    return redirect('/')

def customer_logout (request):
    del request.session['customer_mobile']
    return redirect('/')