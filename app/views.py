from .models import *
from .serializers import *
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect, HttpResponse
@api_view(['GET'])
def home(request):
     return render(request, "index.html", {})

@api_view(['GET'])
def blog(request):
     return render(request, "blog.html", {})

@api_view(['GET'])
def checkout(request):
     return render(request, "checkout.html", {})
 
@api_view(['GET', 'POST'])
def contact(request):
     return render(request, "contact.html", {})
 
@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        name = request.POST.get['name']
        lastname = request.POST.get['last']
        password = request.POST.get['password']
        email = request.POST.get['email']
        # gender = request.POST.get['gender']

        user = CustomUser(name=name, lastname=lastname, password=password, email=email)
        user.save()

        return redirect('login')

    return render(request, 'register.html')

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        if name and password:
            try:
                user = CustomUser.objects.get(name=name, password=password)
                return redirect('home')
            except CustomUser.DoesNotExist:
                wrong_password = True
                return render(request, 'login.html', {'wrong_password': wrong_password})
        else:
            error_message = "Username or password is missing."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')
 
@api_view(['GET'])
def regular_page(request):
     return render(request, "regular-page.html", {})
 
@api_view(['GET', 'POST'])
def shop(request):
     return render(request, "shop.html", {})
 
@api_view(['GET', 'POST'])
def single_blog(request):
     return render(request, "single-blog.html", {})
 
@api_view(['GET', 'POST'])
def single_product_details(request):
     return render(request, "single-product-details.html", {})
