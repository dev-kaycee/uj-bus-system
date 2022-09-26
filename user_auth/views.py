from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from schedule.models import Bus, Trip

# from user_auth.models import Student
from .forms import NewUserForm


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # TODO user validation
        user_obj = authenticate(request, username=username, password=password) 

        if user_obj is not None:
            login(request, user_obj)
            user = request.user.username
            print(user)
            return HttpResponseRedirect(reverse('user_auth:home'))
        else:
            return render(request, 'login.html')
            
            

class RegisterView(View):
    def get(self, request):
        form = NewUserForm()
        return render(request=request, template_name="register.html", context={"register_form":form})
    
    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("user_auth:login")
        print(form)
        messages.error(request, "Unsuccessfull. invalid details")
        # form = NewUserForm()
        return render(request=request, template_name="register.html", context={"register_form":form})

class HomeView(View):
    model = Trip
    # template_name = 'home.html'
    def get(self, request):
        all_posts_qs = Trip.objects.all()
        return render(request, template_name="home.html", context={"buses":all_posts_qs})

class LogoutView(View):
    mode = Bus
    pass