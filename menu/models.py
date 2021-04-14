from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    photo = models.ImageField(default='default.jpg', upload_to='menu', null=True, blank=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    approx_time = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('view_menu')

    def __str__(self):
        return f"{self.name} "

class Cart(models.Model):
    item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    quantity = models.IntegerField(blank=True,null=True)
    notes = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=20,blank=True,null=True,default='Not Done')

    def __str__(self):
        return f"{self.item.name}"




