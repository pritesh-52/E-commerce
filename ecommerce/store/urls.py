"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from .import views
from store.controller import authview,cart,wishlist,checkout,order
urlpatterns = [
    path('',views.home,name="home"),
    path('collections',views.collections,name="collections"), #colletion page 
    path('collections/<str:slug>',views.collectionsview,name="collectionsview"), #collection view of particlur product
    path('collections/<str:prod_slug>/<str:id>',views.productview,name="productview"), #see product view 
    path('product-list',views.productlistAjax,name="productlistAjax"),
    path('seacrhproduct',views.seacrhproduct,name="seacrhproduct"),
    path('register/',authview.register,name="register"),   #Register user new foler create sperte
    path('login/',authview.loginpage,name="login"),  #login user new folder
    path('logout/',authview.logoutpage,name="logout") , #logut user folder create
    path('add-to-cart',cart.addtocart,name="addtocart"), #add to cart function
    path('cart/',cart.viewcart,name="cart"),  #view cart page 
    path('update-cart',cart.updatecart,name="updatecart"), #update cart value 
    path('delete-cart-item',cart.deletecartitem,name="deletecartitem"), #delete cart item 
    path('wishlist',wishlist.index,name="wishlist"), #wishlist page create 
    path('add-to-wishlist',wishlist.addtowishlist,name="addtowishlist"),  #add to item in wishlist 
    path('delete-wishlist-item',wishlist.deletewishlishitem,name="deletewishlishitem"), #delte item from wishlist
    path('checkout',checkout.index,name="checkout"), #checkout page 
    path('place-order',checkout.placeorder,name="placeorder"), #place order cod method page
    path('proceed-to-pay',checkout.razorpaycheck,name="razorpaycheck"), #razorpay integrate payment
    path('my-orders',order.index,name="myorder"), #show all my orders 
    path('view-order/<str:t_no>',order.vieworder,name="orderview"),

    
    

    
]
