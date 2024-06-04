from rest_framework import serializers
from listings.models import ListingTender

class ListingTenderSerializer(serializers.ModelSerializer):
    ministry_name = serializers.CharField(source='source_ministry.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    location_name = serializers.CharField(source='location.name', read_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)
    fields_name = serializers.CharField(source='fields.name', read_only=True)
    
    class Meta:
        model = ListingTender
        fields = [
            'id', 'title', 'source_company', 'ministry_name', 'department_name', 
            'fields_name', 'type', 'opendate', 'closedate', 'attpdf', 'attimage', 
            'description', 'location_name', 'city_name', 'created_at', 'updated_at'
        ]
        

class TestingSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id',read_only=True)
    title = serializers.CharField(source='source_ministry.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    location_name = serializers.CharField(source='location.name', read_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)
    fields_name = serializers.CharField(source='fields.name', read_only=True)
    
    class Meta:
        model = ListingTender
        fields = [
            'id', 'title', 'source_company', 'ministry_name', 'department_name', 
            'fields_name', 'type', 'opendate', 'closedate', 'attpdf', 'attimage', 
            'description', 'location_name', 'city_name', 'created_at', 'updated_at'
        ]