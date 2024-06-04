from django.shortcuts import render, redirect, get_object_or_404
from listings.models import ListingTender, Department, City
from listings.forms import TenderSearchForm
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from users.forms import RegisterForm, LoginForm
from django.http import JsonResponse

def index(request):
    tenders = ListingTender.objects.all().order_by('-created_at')
    return render(request, 'frontend/index.html', {
        'tenders': tenders,
        })
    
    
def tenders(request):
    tenders_list = ListingTender.objects.all().order_by('-created_at')
    paginator = Paginator(tenders_list, 10)  # Show 10 tenders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = tenders_list.count()
    # Initialize the search filter form
    form = TenderSearchForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data['title']:
            tenders_list = tenders_list.filter(title__icontains=form.cleaned_data['title'])
        if form.cleaned_data['company']:
            tenders_list = tenders_list.filter(company__icontains=form.cleaned_data['company'])
        if form.cleaned_data['ministry']:
            tenders_list = tenders_list.filter(source_ministry=form.cleaned_data['ministry'])
        if form.cleaned_data['department']:
            tenders_list = tenders_list.filter(department=form.cleaned_data['department'])
        if form.cleaned_data['fields']:
            tenders_list = tenders_list.filter(fields=form.cleaned_data['fields'])
        if form.cleaned_data['tender_type']:
            tenders_list = tenders_list.filter(type=form.cleaned_data['tender_type'])
        if form.cleaned_data['regionstate']:
            tenders_list = tenders_list.filter(location=form.cleaned_data['regionstate'])
        if form.cleaned_data['city']:
            tenders_list = tenders_list.filter(city=form.cleaned_data['city'])
        
        
        # Reinitialize paginator with filtered tender list
        paginator = Paginator(tenders_list, 10)
        page_obj = paginator.get_page(page_number)
    
    return render(request, 'frontend/tenders.html', {
        'page_obj': page_obj,
        'form': form, # Pass the form to the template
        'count' : count,
    })


def tender_page(request, slug):
    tender = get_object_or_404(ListingTender, slug=slug)
    print(tender.attimage.url)
    # Initialize the search filter form
    form = TenderSearchForm(request.GET or None)
    
    return render(request, 'frontend/tender_page.html', {
        'tender': tender,
        'form': form
    })
    
    
def register(request):
    if request.user.is_authenticated:
        return redirect('frontend:index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request, user)  # Log the user in after successful registration
            return redirect('listings:tenders')
    else:
        form = RegisterForm()
    return render(request, 'frontend/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('frontend:index')
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('listings:tenders')
    else:
        form = LoginForm()
    return render(request, 'frontend/login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('frontend:index')
    return redirect('frontend:index')


def tenders_search(request):
    tenders = ListingTender.objects.all()
    
    form = TenderSearchForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data['title']:
            tenders = tenders.filter(title__icontains=form.cleaned_data['title'])
        if form.cleaned_data['company']:
            tenders = tenders.filter(source_company__icontains=form.cleaned_data['company'])
        if form.cleaned_data['ministry']:
            tenders = tenders.filter(source_ministry=form.cleaned_data['ministry'])
        if form.cleaned_data['department']:
            tenders = tenders.filter(department=form.cleaned_data['department'])
        if form.cleaned_data['fields']:
            tenders = tenders.filter(fields=form.cleaned_data['fields'])
        if form.cleaned_data['tender_type']:
            tenders = tenders.filter(type=form.cleaned_data['tender_type'])
        if form.cleaned_data['regionstate']:
            tenders = tenders.filter(location=form.cleaned_data['regionstate'])
        if form.cleaned_data['city']:
            tenders = tenders.filter(city=form.cleaned_data['city'])

    count = tenders.count()
    paginator = Paginator(tenders, 10)  # Show 10 tenders per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'frontend/tenders.html', {
        'page_obj': page_obj,
        'form': form,
        'count' : count
        })
    