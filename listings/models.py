from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field
import bleach
import uuid
from django.utils.text import slugify

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
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    source_company = models.CharField(max_length=255, null=True, blank=True)
    source_ministry = models.ForeignKey(Ministry, null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    fields = models.ForeignKey(Fields, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=15, choices=TENDER_TYPE_CHOICES, default=OPEN)
    opendate = models.DateTimeField(default=timezone.now)
    closedate = models.DateTimeField(default=timezone.now)
    attpdf = models.FileField(upload_to='tenders/pdfs/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    attimage = models.ImageField(upload_to='tenders/images/', default="fallback.png", null=True, blank=True)
    description = CKEditor5Field('Description', config_name='extends', null=True, blank=True)
    location = models.ForeignKey(StateOrRegion, null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set to the current date and time when object is created
    updated_at = models.DateTimeField(auto_now=True)
    old_slugs = models.TextField(blank=True, default='')


    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = ListingTender.objects.get(pk=self.pk)
            if self.title != old_instance.title:
                self.old_slugs += f'{old_instance.slug},'
                self.slug = self.generate_unique_slug()
        else:
            self.slug = self.generate_unique_slug()
            
        allowed_tags = bleach.sanitizer.ALLOWED_TAGS.union({'p', 'span', 'div', 'br', 'strong', 'em', 'ul', 'ol', 'li'})
        allowed_attributes = {'*': ['style']}
        self.description = bleach.clean(self.description, tags=allowed_tags, attributes=allowed_attributes)
        super(ListingTender, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        base_slug = slugify(self.title)
        slug = base_slug
        num = 1
        while ListingTender.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{num}'
            num += 1
        return slug        

        
    def __str__(self):
        return self.title