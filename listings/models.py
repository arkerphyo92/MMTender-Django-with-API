from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.

class Ministry(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Fields(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class StateOrRegion(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    stateorregion = models.ForeignKey(StateOrRegion, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ListingTender(models.Model):
    OPEN = 'Opened Tender'
    CLOSED = 'Closed Tender'
    
    TENDER_TYPE_CHOICES = [
        (OPEN, 'Open Tender'),
        (CLOSED, 'Closed Tender')
    ]
    
    title = models.CharField(max_length=255)
    source_company = models.CharField(max_length=255, null=True, blank=True)
    source_ministry = models.ForeignKey(Ministry, null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    fields = models.ForeignKey(Fields, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=15, choices=TENDER_TYPE_CHOICES, default=OPEN)
    opendate = models.DateField()
    closedate = models.DateField()
    attpdf = models.FileField(upload_to='tenders/pdfs/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    attimage = models.ImageField(upload_to='tenders/images/', default="fallback.png", null=True, blank=True)
    description = RichTextField()
    location = models.ForeignKey(StateOrRegion, null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set to the current date and time when object is created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title