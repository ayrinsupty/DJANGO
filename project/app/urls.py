from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login', views.handlelogin, name='handlelogin'),
    path('signup', views.handlesignup, name='handlesignup'),
]