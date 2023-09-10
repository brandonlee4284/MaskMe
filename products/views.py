from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, AboutUs, Customize, Home, ConfirmationPage, Promo,Test,Payment, Customize1, Customize2, Customize3

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

def home(request):
    homes = Home.objects.all()
    return render(request, 'home.html',
                  {'homes': homes})

def about_us(request):
    aboutus = AboutUs.objects.all()
    return render(request, 'aboutUs.html',
                  {'aboutus': aboutus})


def customize(request):
    customizes = Customize.objects.all()
    return render(request, 'customize.html',
                  {'customizes': customizes})

def confirmation_page(request):
    confirmation_pages = ConfirmationPage.objects.all()
    return render(request, 'confirmation_page.html',
                  {'confirmation_pages': confirmation_pages})

def promo(request):
    promos = Promo.objects.all()
    return render(request, 'promo.html',
                  {'promos': promos})

def test(request):
    tests = Test.objects.all()
    return render(request, 'test.html',
                  {'test': tests})

def payment(request):
    payments = Payment.objects.all()
    return render(request, 'payment.html',
                  {'payment': payments})

def customize1(request):
    customizes1 = Customize1.objects.all()
    return render(request, 'customize1.html',
                  {'customizes1': customizes1})

def customize2(request):
    customizes2 = Customize2.objects.all()
    return render(request, 'customize2.html',
                  {'customizes2': customizes2})

def customize3(request):
    customizes3 = Customize3.objects.all()
    return render(request, 'customize3.html',
                  {'customizes3': customizes3})