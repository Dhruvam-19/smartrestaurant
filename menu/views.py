from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import *
from django.db.models import Sum

from django.db.models import F
# Create your views here.
class Delete_cartitem(DeleteView):
    model =Cart
    success_url = '/menu/view_cart'


class Create_menu(CreateView):
    model = Menu
    fields = ['name','description','photo','type','price','approx_time']

def view_menu(request):
    object = Menu.objects.all().order_by('type')
    return render(request,"menu/view_menu.html",{'object':object})

def add_to_cart(request,id):
    if request.method == 'POST':
        menu_info = Menu.objects.get(id=id)
        item_info = Cart(item=menu_info,quantity=request.POST['quantity'],notes=request.POST['remarks'],user=request.user)
        #item_info.item.add(menu_info)
        item_info.save()
        return redirect('view_menu')
    else:
        return render(request,"menu/view_menu.html",{})

def view_cart(request):
    #Cart.objects.annotate(price=F('quantity') * F('item.price'))
    object = Cart.objects.filter(user = request.user.id).all()
    object1 = Cart.objects.all()
    #total = Cart.objects.filter(user = request.user.id).all().aggregate(Sum(''))
    total_time = Cart.objects.filter(user = request.user.id).all().annotate(total_time=Sum('item__approx_time'))

    return render(request,"menu/view_cart.html",{'object':object,'total_time':total_time,
                                                 'object1':object1})
