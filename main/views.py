from django.shortcuts import render
from django.http import HttpResponse
from .models import Diet

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def delivery(request):
    return render(request, 'main/delivery.html')


def faq(request):
    return render(request, 'main/faq.html')


def info(request):
    return render(request, 'main/info.html')


def lk(request):
    return render(request, 'main/lk.html')


def menu(request):
    diets = Diet.objects.all()
    return render(request, 'main/menu.html',{'title':'Меню','diets':diets })

def standart_menu(request):
    diets=Diet.objects.filter(category=3)
    return render(request, 'main/menu.html', {'title': 'Меню', 'diets': diets})
def vegan_menu(request):
    diets=Diet.objects.filter(category=4)
    return render(request, 'main/menu.html', {'title': 'Меню', 'diets': diets})

def order_step1(request):
    return render(request, 'main/order_step1.html')


def order_step2(request):
    return render(request, 'main/order_step2.html')


def order_step3(request):
    return render(request, 'main/order_step3.html')


def order_step4(request):
    return render(request, 'main/order_step4.html')


