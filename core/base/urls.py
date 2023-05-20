
from django.urls import path ,include
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),

    #main pages
    #path('services/', views.services, name='services'),
    #path('services/<int:id>', views.service_details, name='service_details'),
    #path('FAQs/', views.FAQs, name='FAQs'),
    #path('contact/', views.contact, name='contact'),
    #path('aboutus/', views.aboutus, name='aboutus'),
    #path('familyreunion/', views.familyreunion, name='familyreunion'),

    #auth
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),


    
]