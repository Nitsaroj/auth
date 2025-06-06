from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout
from .form import RegisterFrom

def register_view(request):
   if request.method == 'POST':
      form = RegisterFrom(request.POST)
      if form.is_valid():
         user= form.save(commit=False)
         user.set_password(form.cleaned_data['password'])
         user.save()
         return redirect('login')
   else:
       form=RegisterFrom()
   return render(request,'register.html',{'form':form})

def login_view(request):
   if request.method == 'POST':
     username= request.POST['username']
     password=request.POST['password']
     user= authenticate(request,username=username,password=password)
     if user:
        login(request,user)
        return redirect('home')
   return render(request,'login.html')


def logout_view(request):
   logout(request)
   return redirect('login')

def home(request):
   return render(request,'home.html',{'user': request.user})