from django.shortcuts import render, redirect
from django import views
from authApp.forms import RegisterForm, LoginForm, ProfileEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from authApp.models import User

# Create your views here.

class RegisterView(views.View):
    
    def get(self,request):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request,'register.html',context)
    
    def post(self,request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():            
            new_user = User.objects.create(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['password']
            )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            context = {
                'form': form
            }
            messages.success(request,'You have registered successfully')
            return redirect('authApp:login')
        else:
            messages.error(request, "Form is not valid")
            form = RegisterForm()
            context = {
                'form': form
            }
            return render(request,'register.html',context)
        

class LoginView(views.View):
    
    def get(self,request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request,'login.html',context)
    
    def post(self,request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            if user and user.check_password(form.cleaned_data['password']):
                login(request,user)
                messages.success(request,'You have successfully logged in')
                return redirect('ads:ads_list')
            else:
                messages.error(request, 'Please, enter correct credentials')
                return render(request, 'login.html', {'form': form})
                
        else:
            return render(request,'login.html',{'form': form})


class LogoutView(LoginRequiredMixin, views.View):
    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'You have not logged in')
        logout(request)
        return redirect('ads:ads_list')

class ProfileEditView(LoginRequiredMixin,views.View):
    def get(self,request):
        form = ProfileEditForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request,'profileEdit.html',context)
    
    def post(self,request):
        form = ProfileEditForm(instance=request.user,
                               data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully updated your profile')
            return redirect('ads:ads_list')
        else:
            form = ProfileEditForm(instance=request.user)
            context = {
                'form': form
            }
            return render(request,'profileEdit.html',context)





