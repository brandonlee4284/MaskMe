from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('aboutus', views.about_us),
    path('customize', views.customize),
    path('confirmation_page', views.confirmation_page),
    path('promo', views.promo),
    path('payment', views.payment),
    path('test', views.test),
    path('customize1', views.customize1),
    path('customize2', views.customize2),
    path('customize3', views.customize3)

]