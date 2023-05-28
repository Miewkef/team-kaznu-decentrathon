from django.shortcuts import render, redirect
from .models import Price


def index(request):
    prices = Price.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Глав стр сайта', 'prices': prices}) 


def gadgetron(request):
    return render(request, 'main/gadgetron.html')


def nodereal(request):
    return render(request, 'main/nodereal.html')

def titan(request):
    return render(request, 'main/titan.html')

def volbot(request):
    return render(request, 'main/volbot.html')

def thorax(request):
    return render(request, 'main/thorax.html')

def neuronet(request):
    return render(request, 'main/neuronet.html')

def zenon(request):
    return render(request, 'main/zenon.html')

def cogsworth(request):
    return render(request, 'main/cogsworth.html')