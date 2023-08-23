from django.contrib import admin
from django.urls import path
from devn import views

urlpatterns = [
    path("", views.index, name='devn'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
     path("app-ads.txt", views.appads, name='appads'),
]
