from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def add_product(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        if request.method == "POST":
            product_name=request.POST.get('product_name')
            price=request.POST.get('price')
            discount=request.POST.get('discount')
            if discount == "":
                discount = None
            image_1 = request.FILES.get("image_1")
            image_2 = request.FILES.get("image_2")
            image_3 = request.FILES.get("image_3")
            image_4 = request.FILES.get("image_4")
            discription=request.POST.get('editordata')
            Product(
                product_name=product_name,
                price=price,
                discount=discount,
                image_1=image_1,
                image_2=image_2,
                image_3=image_3,
                image_4=image_4,
                discription=discription
            ).save()
            return redirect('/product/add_product/')

        return render(request, 'product/add_product.html')
    else:
        return render(request,'login.html')
    
def all_product(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        if "Active" in request.POST:
            id=request.POST.get('id')
            ac=Product.objects.get(id=id)
            ac.status='0'
            ac.save()
        elif "Deactive" in request.POST:
            id=request.POST.get('id')
            ac=Product.objects.get(id=id)
            ac.status='1'
            ac.save()  
        p = Product.objects.all()
        context={
            'p':p
        }
        return render(request, 'product/all_product.html',context)
    else:
        return render(request,'login.html')
    



def edit_product(request, id):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        p = Product.objects.get(id=id)
        if request.method == "POST":
            product_name=request.POST.get('product_name')
            price=request.POST.get('price')
            discount=request.POST.get('discount')
            if discount == "":
                discount = None
            discription=request.POST.get('editordata')
            image_1 = request.FILES.get("image_1")
            if image_1 == None:
                i=Product.objects.get(id=id)
                image_1=i.image_1
                #print(image_1)
            image_2 = request.FILES.get("image_2")
            if image_2 == None:
                i=Product.objects.get(id=id)
                image_2=i.image_2
                #print(image)
            image_3 = request.FILES.get("image_3")
            if image_3 == None:
                i=Product.objects.get(id=id)
                image_3=i.image_3
                #print(image)
            image_4 = request.FILES.get("image_4")
            if image_4 == None:
                i=Product.objects.get(id=id)
                image_4=i.image_4
                #print(image)
            Product(
                product_name=product_name,
                price=price,
                discount=discount,
                id=id,
                image_1=image_1,
                image_2=image_2,
                image_3=image_3,
                image_4=image_4,
                discription=discription
            ).save()
            messages.success(request,"Product Edit Succesfully")
            return redirect('/product/all_product/')
        context={
            'p':p
        }
        return render(request, 'product/edit_product.html',context)
    else:
        return render(request,'login.html')
    
def add_category(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        dc=Category.objects.filter().all()
        context={
            'dc':dc,     
        }
        if request.method == "POST":
            if "Add" in request.POST:
                name=request.POST.get('name')
                admin_id = request.POST.get('admin_id')
                Category.objects.create(
                    category_name=name,
                )
                messages.success(request,"Category Added Succesfully")
                return redirect ('/product/add_category/')
            elif "Edit" in request.POST:
                name=request.POST.get('name')
                id=request.POST.get('id')
                edit_category=Category.objects.get(id=id)
                edit_category.category_name=name
                edit_category.save()
                messages.success(request,"Category Edit Successfully")
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Category.objects.get(id=id).delete()
                messages.success(request,"Category Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                ac=Category.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                ac=Category.objects.get(id=id)
                ac.status='1'
                ac.save()      
        return render(request, 'product/add_category.html',context)
    else:
        return render(request,'login.html')
    

def select_category(request,id):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={
            'p':Product.objects.get(id=id),
            'c':Category.objects.all(),
            'sc':Select_category.objects.all(),
        }
        return render(request, 'product/select_category.html',context)
    else:
        return render(request,'login.html')