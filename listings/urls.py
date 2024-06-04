from django.contrib import admin
from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.tenders, name='dashboard'),
    path('tenders/', views.tenders, name='tenders'),
    path('add-tender/', views.add_tender, name='add_tender'),
    path('edit-tender/<int:id>', views.edit_tender, name='edit_tender'),
    path('delete-tender/<int:id>', views.delete_tender, name='delete_tender'),
    path('check_permissions/', views.check_permissions, name='check_permissions'),
]
