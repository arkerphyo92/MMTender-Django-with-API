from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('tenders/', views.tenders, name='tenders'),
    path('tender_list/', views.tender_list, name='tender_list'),
    path('tender-page/<int:id>', views.tender_page, name='tender_page'),
]
