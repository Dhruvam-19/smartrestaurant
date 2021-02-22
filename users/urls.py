from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProfileUpdateView

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.create_profile.as_view(template_name='users/profile.html'),name='profile'),
    path('update/<int:pk>',ProfileUpdateView.as_view(template_name='users/profile.html'),name='update_profile'),
    path('view_profile/<int:profile_id>',views.view_profile,name='view_profile'),
]