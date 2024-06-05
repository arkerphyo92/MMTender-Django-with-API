from django.shortcuts import render, get_object_or_404
from listings.models import ListingTender, Department, City
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import ListingTenderSerializer, TestingSerializer

from django.http import JsonResponse

# Create your views here.

class TenderList(APIView):
    def get(self, request):
        tenders = ListingTender.objects.all().order_by('-created_at')
        serializer = ListingTenderSerializer(tenders, many=True)
        return Response({"Tenders": serializer.data}, status=status.HTTP_200_OK)


class TenderDetail(APIView):
    def get(self, request, id):
        try:
            tender = ListingTender.objects.get(pk=id)
        except ListingTender.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListingTenderSerializer(tender)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TenderList(APIView):
    def get(self, request):
        tenders = ListingTender.objects.all().order_by('-created_at')
        serializer = ListingTenderSerializer(tenders, many=True)
        return Response({"Tenders": serializer.data}, status=status.HTTP_200_OK)


class TenderDetail(APIView):
    def get(self, request, id):
        try:
            tender = ListingTender.objects.get(pk=id)
        except ListingTender.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListingTenderSerializer(tender)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DepartmentList(APIView):
    def get(self, request, ministry_id):
        departments = Department.objects.filter(ministry_id=ministry_id).values('id', 'name')
        return Response(departments, status=status.HTTP_200_OK)


class CityList(APIView):
    def get(self, request, location_id):
        cities = City.objects.filter(stateorregion_id=location_id).values('id', 'name')
        return Response(cities, status=status.HTTP_200_OK)
    

#---- Training --------------------------------
@api_view()
def allapitenders(request):
    try:
        tenders = ListingTender.objects.all()
    except tenders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ser = TestingSerializer(tenders, many=True)
    return Response(ser.data)

@api_view()
def singleapitenders(request,id):
    try:
        tender = ListingTender.objects.get(pk=id)
    except tender.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ser = TestingSerializer(tender)   
    return JsonResponse(ser.data)