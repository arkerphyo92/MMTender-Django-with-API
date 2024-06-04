from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('tenders/', views.tenders, name='tenders'),
    path('tenders/search/', views.tenders_search, name='tenders_search'),
    path('tenders/<slug:slug>/', views.tender_page, name='tender_page'),
]
