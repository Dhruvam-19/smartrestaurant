from django.urls import path
from . import views

urlpatterns = [
    path('add_menu/',views.Create_menu.as_view(template_name='menu/add_menu.html'),name='add_menu'),
    path('view_menu',views.view_menu,name='view_menu'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
    path('view_cart',views.view_cart,name='view_cart'),
    path('delete/<int:pk>',views.Delete_cartitem.as_view(),name='delete_cartitem')
]