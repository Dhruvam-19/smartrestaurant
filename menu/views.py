from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import *
from django.db.models import F
# Create your views here.
class Delete_cartitem(DeleteView):
    model =Cart
    success_url = '/menu/view_cart'


class Create_menu(CreateView):
    model = Menu
    fields = ['name','description','photo','type','price']

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

def view_cart(request):
    #Cart.objects.annotate(price=F('quantity') * F('item.price'))
    object = Cart.objects.filter(user = request.user.id).all()
    #total = Cart.objects.filter(user = request.user.id).all().aggregate(Sum(''))

    return render(request,"menu/view_cart.html",{'object':object})
