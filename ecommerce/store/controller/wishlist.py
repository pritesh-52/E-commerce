from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import  HttpResponse, JsonResponse
from django.contrib import messages
from store.models import Product,Cart,wishlist
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    wishlistitem=wishlist.objects.filter(user=request.user)
    context={'wishlistitem':wishlistitem}
    return render(request,'store/wishlist.html',context)

def addtowishlist(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product.objects.get(id=prod_id)
            if (product_check):
                if (wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':"Product already in wishlist"})
                else:
                    wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"Product added to wishlist"})
            else:   
                return JsonResponse({'status':"No such product found"})
        
        else:
            return JsonResponse({'status',"Login to continue"})


    return redirect('/')   

def deletewishlishitem(request):
    if request.method=="POST":
        prod_id=int(request.POST.get('product_id'))
        if(wishlist.objects.filter(user=request.user,product_id=prod_id)):
            wishlistitem=wishlist.objects.get(product_id=prod_id,user=request.user)
            wishlistitem.delete()
            return JsonResponse({'status':'Removed Successfully'})
    return redirect('/')
