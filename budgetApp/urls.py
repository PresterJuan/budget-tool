from django.contrib import admin
from django.urls import path, include
from budgetApp import urls, views

urlpatterns = [
    path('',views.index, name='home'),
    path('test',views.test, name='test'),
]
