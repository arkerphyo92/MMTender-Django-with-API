from django import forms
from .models import ListingTender, Ministry, Department, Fields, StateOrRegion, City
from django_ckeditor_5.fields import CKEditor5Field

class ListingTenderForm(forms.ModelForm):
    description = CKEditor5Field('Description', config_name='extends')
    # description = forms.CharField(widget=CKEditor5UploadingWidget(config_name='default'))
    
    class Meta:
        model = ListingTender
        fields = [
            'title', 'source_company', 'source_ministry', 'department', 
            'fields', 'type', 'opendate', 'closedate', 'attpdf', 'attimage', 'description',
            'location', 'city'
        ]
        labels = {
            'title': 'Title',
            'source_company': 'Company',
            'source_ministry': 'Ministry',
            'department': 'Department',
            'fields': 'Fields',
            'type': 'Type',
            'opendate': 'Tender Open Date',
            'closedate': 'Tender Close Date',
            'attpdf': 'PDF',
            'attimage': 'Image',
            'location': 'Location',
            'city': 'City',
            'description': 'Description',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'source_company': forms.TextInput(attrs={'class': 'form-control'}),
            'source_ministry': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'fields': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'opendate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'closedate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            # 'opendate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'closedate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'attpdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'attimage': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }


class TenderSearchForm(forms.Form):
    title = forms.CharField(required=False, label='Title')
    company = forms.CharField(required=False, label='Company')
    ministry = forms.ModelChoiceField(queryset=Ministry.objects.all(), required=False, label='Ministry', widget=forms.Select(attrs={'class': 'form-control'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False, label='Department', widget=forms.Select(attrs={'class': 'form-control'}))
    fields = forms.ModelChoiceField(queryset=Fields.objects.all(), required=False, label='Fields')
    tender_type = forms.ChoiceField(choices=[('', 'Any'), ('Opened Tender', 'Open Tender'), ('Closed Tender', 'Closed Tender')], required=False, label='Tender Type')
    regionstate = forms.ModelChoiceField(queryset=StateOrRegion.objects.all(), required=False, label='StateOrRegion')
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, label='City')
    class Meta:
        fields = [
            'title', 'company', 'ministry', 'department', 'fields', 'tendertype','regionstate', 'city'
        ]
        labels = {
            'title' : 'Title',
            'company' : 'Company',
            'ministry' : 'Ministry',
            'department' : 'Department',
            'fields' : 'Fields',
            'tendertype' : 'Tender Type',
            'regionstate' : 'Region or State',
            'city' : 'City',
        }
        
    def __init__(self, *args, **kwargs):
        super(TenderSearchForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Search Keywords'})
        self.fields['company'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Company Name'})
        self.fields['ministry'].widget.attrs.update({'class': 'form-control'})
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['fields'].widget.attrs.update({'class': 'form-control'})
        self.fields['tender_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['regionstate'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
