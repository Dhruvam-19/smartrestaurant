from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .models import *

# Create your views here.
def home(request):
    return render(request,"users/home.html")


class create_profile(CreateView):
    model =  Profile
    fields = ['image','first_name','middle_name','last_name','father_first_name',
              'father_middle_name','father_last_name','date_of_birth','joining_date',
              'email','phone_number1','phone_number2','address_lane1','address_lane2',
              'address_lane3','state','country','adharcard_number','document1']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['image','first_name','middle_name','last_name','father_first_name',
              'father_middle_name','father_last_name','date_of_birth','joining_date',
              'email','phone_number1','phone_number2','address_lane1','address_lane2',
              'address_lane3','state','country','adharcard_number','document1' ]
    template_name = "users/profile.html"

def view_profile(request,profile_id):
    object =Profile.objects.filter(pk = profile_id).first()
    return render(request,"users/view_profile.html",{'object':object})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST);
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f"{username} is created successfully")
            return redirect('login')
        else :
            return render(request, "users/register.html", {
                "form": form
            })
    form=UserRegisterForm();
    return render(request,"users/register.html",{
        "form":form
    })
