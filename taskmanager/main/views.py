from django.shortcuts import render, redirect
from .models import Price
from .forms import PriceForm


def index(request):
    prices = Price.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Глав стр сайта', 'prices': prices}) 


def about(request):
    return render(request, 'main/about.html')


def price(request):
    return render(request, 'main/price.html')

def set(request):
    error=''
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма неверна'

    form = PriceForm()
    context = {
        "form": form,
        'error': error, 
    }
    return render(request, 'main/set.html', context)