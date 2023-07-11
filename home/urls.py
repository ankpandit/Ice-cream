from django.contrib import admin
from django.urls import path , include 
from home import views 

admin.site.site_header = "IceCream -Admin Panel"
admin.site.site_title = "IceCream -Admin Panel"
admin.site.index_title = "Welcome to IceCream -Admin Panel"

urlpatterns = [
    path('',views.index ,name='home') ,
    path('about',views.about ,name='home') ,
    path('contact',views.contact ,name='home') ,
    path('services',views.services ,name='home')

]
