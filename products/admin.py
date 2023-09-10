from django.contrib import admin
from .models import Product, Offer, AboutUs, Customize, Home, ConfirmationPage, Promo, Test, Payment, Customize1, Customize2, Customize3

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('topic','paragraph','image_url')

class CustomizeAdmin(admin.ModelAdmin):
    list_display = ('message','other')

class HomeAdmin(admin.ModelAdmin):
    list_display = ('message','video_url')

class ConfirmationPageAdmin(admin.ModelAdmin):
    list_display = ('message','other')

class PromoAdmin(admin.ModelAdmin):
    list_display = ('message','other')

class TestAdmin(admin.ModelAdmin):
    list_display = ('message','other')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('message','other')

class Customize1Admin(admin.ModelAdmin):
    list_display = ('message','other')

class Customize2Admin(admin.ModelAdmin):
    list_display = ('message','other')

class Customize3Admin(admin.ModelAdmin):
    list_display = ('message','other')
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(Customize,CustomizeAdmin)
admin.site.register(Home,HomeAdmin)
admin.site.register(ConfirmationPage,ConfirmationPageAdmin)
admin.site.register(Promo,PromoAdmin)
admin.site.register(Test,TestAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Customize1,Customize1Admin)
admin.site.register(Customize2,Customize2Admin)
admin.site.register(Customize3,Customize3Admin)




