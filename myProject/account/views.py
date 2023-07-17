from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomEmailAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from account.models import CustomUser

User = get_user_model()

# Create your views here.

def signupaccount(request):
    if request.method == 'POST':
        try:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return render(request, 'account/signupaccount.html', {'form': form, 'message': 'Account created successfully','alert':'alert-success'})
            else:
                return render(request, 'account/signupaccount.html', {'form': form, 'message': form.errors, 'alert':'alert-danger'})
        except Exception as e:
            return render(request, 'account/signupaccount.html', {'form': form, 'message': e})
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signupaccount.html', {'form': form})

def loginaccount(request):  
    if request.method == 'POST':
        form = CustomEmailAuthenticationForm(request.POST)
        if form.is_valid():
            print("form dogru")
            email = request.POST["email"]
            password = request.POST["password"]
            print(email,password)
            user = CustomUser.objects.filter(email=email).first()
            if user is None:
                 return render(request, 'account/loginaccount.html', {'form': form, 'message': 'Email not fount', 'alert':'alert-danger'})
            if user.check_password(password):
                login(request, user)
                return redirect('home')
            else :
                return render(request, 'account/loginaccount.html', {'form': form, 'message': 'Invalid username or password', 'alert':'alert-danger'})
                
        else:
            return render(request, 'account/loginaccount.html', {'form': form, 'message': form.errors, 'alert':'alert-danger'})
    else:
        form = CustomEmailAuthenticationForm()
    return render(request, 'account/loginaccount.html', {'form': form})
    

def logoutaccount(request):
    logout(request)
    return redirect('home')