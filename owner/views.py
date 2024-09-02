from django.shortcuts import render,redirect
from product.models import *
# Create your views here.
def owner_dashboard(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        return render(request, 'owner/owner_dashboard.html')
    else:
        return redirect('/login/')
    

def print_address(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        return render(request, 'owner/print_address.html')
    else:
        return redirect('/login/')
    
