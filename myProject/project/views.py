from urllib import request
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Menu, Rezervation, Table,Cart,Comment
# import messages
from django.contrib import messages


# Create your views here.

def home(request):
    menu = Menu.objects.all()
    comment = Comment.objects.all()
    return render(request,'home.html',{'menu':menu, 'comment':comment})

def menu(request):
    menu = Menu.objects.all()
    return render(request,'menu.html',{'menu':menu})    

def about(request):
    return render(request,'about.html')

def bookTable(request):
    tables = Table.objects.all()
    rezervations=Rezervation.objects.all()
    if request.method=='POST':
        try:
            name = request.POST['name']
            surname = request.POST['surname']
            email = request.POST['email']
            phoneNumber = request.POST['phoneNumber']
            date = request.POST['date']
            time = request.POST['time']
            people = request.POST['people']
            table =Table.objects.get(tableNumber=request.POST['table_number'])
            table.is_published = False
            table.save()
            rezervation = Rezervation(name=name,surname=surname,email=email,phoneNumber=phoneNumber,date=date,time=time,people=people,table_number=table)
            rezervation.save()
            return render(request,'bookTable.html',{'tables':tables,'rezervations':rezervations,'message':'Rezervation is successful'})
        except:
            return render(request,'bookTable.html',{'tables':tables,'error':'Rezervation is not successful'})
    return render(request,'bookTable.html',{'tables':tables,'rezervations':rezervations})

def basket(request):
    user=request.user
    cards=Cart.objects.filter(user=user)
    totalPrice=0
    for card in cards:
        totalPrice=totalPrice+ card.menu.price*card.quantity
        
    return render(request,'basket.html', {'cards':cards,'totalPrice':totalPrice})

def deleteBasket(request,id):
    if request.method=='POST':
        user=request.user
        card=Cart.objects.get(id=id)
        card.delete()
        cards=Cart.objects.filter(user=user)
        return redirect('basket')

def addBasket(request,id):
    if request.method=='POST':
        # if user is not logged in, redirect to login page
        if not request.user.is_authenticated:
            return redirect('home')
        # if product is already in the basket, increase the quantity else add the product to the basket
        user=request.user
        menu=Menu.objects.get(id=id)    
        foods = Menu.objects.all()
        card=Cart.objects.filter(user=user,menu=menu)
        if card:
            card=card.first()
            card.quantity+=1
            card.save()
            return render(request,'menu.html',{'menu':foods,'message':'Product is added to the basket'})
        else:
            card=Cart(user=user,menu=menu,quantity=1)
            card.save()
            return render(request,'menu.html',{'menu':foods,'message':'Product is added to the basket'})
        
def payment(request):
    if request.user.is_authenticated:
        user=request.user
        cards=Cart.objects.filter(user=user)
        totalPrice=0
        for card in cards:
            totalPrice=totalPrice+ card.menu.price*card.quantity
        if request.method == 'POST':
            return render(request,'payment.html',{'cards':cards,'totalPrice':totalPrice, 'message':'Order has been received'})
        return render(request,'payment.html',{'cards':cards,'totalPrice':totalPrice})

    else:
        return redirect('home')