from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.http import  HttpResponse,JsonResponse
from .models import *
from django.contrib import messages


def home(request):
    trendingproduct=Product.objects.filter(trending=1)
    context={'trendingproduct':trendingproduct}
    return render(request,'store/index.html',context)


def collections(request):
    category=Category.objects.filter(status=0)
    context={'category':category}
    return render(request,'store/collections.html',context)

def collectionsview(request,slug):
    if (Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'products':products,'category':category}
        return render(request,'store/product/index.html',context)
    else:
        messages.warning(request,'No seacrh category found')
        return redirect('collections')
def productview(request,prod_slug,id):
    if (Product.objects.filter(slug=prod_slug,status=0,id=id)):
        products=Product.objects.filter(slug=prod_slug,status=0,id=id).first()
        context={'products':products}
    else:
        messages.error(request,'No such product found')
        return redirect('collections')
    return render(request,'store/product/view.html',context)


def productlistAjax(request):
    products=Product.objects.filter(status=0).values_list('name',flat=True)
    product_list=list(products)
    return JsonResponse(product_list,safe=False)


def seacrhproduct(request):
    if request.method=='POST':
        seacrhproductterm=request.POST.get('productsearch')
        if seacrhproductterm=="":
             return redirect(request.META.get('HTTP_REFERER'))
        else:
            product=Product.objects.filter(name__contains=seacrhproductterm).first()

            if product:
                return redirect('collections/'+product.slug+'/'+str(product.id))
            else:
                messages.info(request,"No product found again your seacrh product")
                return redirect(request.META.get('HTTP_REFERER'))


    
    return redirect(request.META.get('HTTP_REFERER'))

    


