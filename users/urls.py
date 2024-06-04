from django.contrib import admin
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('', views.users, name='users'),
    # path('assign-group/', views.assign_group, name='assign_group'),
    path('assign-group/', views.select_username, name='select_username'),
    path('assign-group/<int:user_id>/', views.assign_group_id, name='assign_group_id'),
]
