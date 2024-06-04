from django.contrib import admin
from django.urls import path, include
from .views import TenderList, TenderDetail, DepartmentList, CityList
from . import views

app_name = 'api'

urlpatterns = [
    path('tenders/', TenderList.as_view(), name='tender-list'),
    path('tenders/<int:id>/', TenderDetail.as_view(), name='tender-detail'),
    path('departments/<int:ministry_id>/', DepartmentList.as_view(), name='department-list'),
    path('cities/<int:location_id>/', CityList.as_view(), name='city-list'),
    
## Tutorial ##
    path('allapitenders', views.allapitenders, name='allapitenders'),
    path('singleapitenders/<int:id>', views.singleapitenders, name='singleapitenders'),
]
