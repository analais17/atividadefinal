from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def log (request):
     if (request.method == 'POST'):
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None :
             login(request, user)
             messages.add_message(request, messages.INFO, 'Bem vindo de volta!')
             return redirect( '/page/home')
         else:
              messages.add_message(request, messages.INFO, 'Usuário ou senha incorretos!')
              return render(request, 'login.html')

     if(request.method == 'GET'):
          return render(request, 'login.html')


     
          



def home (request):
    return render(request, 'home.html')     





# Create your views here.
