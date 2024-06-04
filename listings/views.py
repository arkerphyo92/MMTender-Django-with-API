from django.shortcuts import render, get_object_or_404
from .forms import ListingTenderForm
from .models import ListingTender, Department, City
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
import logging

# Create your views here.

# -------------------------------------------
# -------------------------------------------

# For Dashboard Pages

# Admin Elements

# For Dashboard Page

@login_required(login_url='frontend:login')
def dashboard(request):
    tenders = ListingTender.objects.all().order_by('-created_at')
    return render(request, 'dashboard/admin/tenders.html', {'tenders': tenders})


# For All Tenders Page from Tenders
@login_required(login_url='frontend:login')
def tenders(request):
    tenders_list = ListingTender.objects.all().order_by('-created_at')
    paginator = Paginator(tenders_list, 10)  # Show 10 tenders per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/admin/tenders.html', {'page_obj': page_obj})


# Add Tender Page from Tenders of Dashboard
@login_required(login_url='frontend:login')
@permission_required('listings.add_listingtender', login_url='frontend:login')
def add_tender(request):
    if request.method == "POST":
        form = ListingTenderForm(request.POST, request.FILES)
        if form.is_valid():
            updatetender = form.save(commit=False)
            updatetender.author = request.user
            updatetender.save()
            #Use this return to avoid multiple submition from dashboard 1
            return HttpResponseRedirect(reverse('listings:add_tender') + '?success=true')
    else:
        form = ListingTenderForm()
    #Use following 2 lines to avoid multiple submition from dashboard 1
    success = request.GET.get('success', 'false') == 'true'
    return render(request, 'dashboard/admin/add_tender.html', {
        'form': form,
        'success': success
    })
    

@login_required(login_url='frontend:login')
@permission_required('listings.change_listingtender', login_url='frontend:login')
def edit_tender(request, id):
    tender = get_object_or_404(ListingTender, pk=id)
    if request.method == "POST":        
        form = ListingTenderForm(request.POST, request.FILES, instance=tender)
        if form.is_valid():
            updatetender = form.save(commit=False)
            updatetender.author = request.user
            updatetender.save()
            #Use this return to avoid multiple submition from dashboard 1
            return HttpResponseRedirect(reverse('listings:edit_tender', args=[id]) + '?success=true')
    else:
        form = ListingTenderForm(instance=tender)
    #Use following 2 lines to avoid multiple submition from dashboard 1
    success = request.GET.get('success', 'false') == 'true'
    return render(request, 'dashboard/admin/edit_tender.html', {
        'form': form,
        'success': success,
        'tender': tender        
    })


@login_required(login_url='login')
def delete_tender(request, id):
    if request.method == 'POST':
        tender = get_object_or_404(ListingTender, pk=id)
        tender.delete()
        # Get the current page number from the request
        page_number = request.POST.get('page', 1)
        return HttpResponseRedirect(f"{reverse('listings:tenders')}?page={page_number}")

    # If the request method is not POST, you may want to handle this case
    return HttpResponseRedirect(reverse('listings:tenders'))
# -------------------------------------------
# -------------------------------------------


logger = logging.getLogger(__name__)

@login_required(login_url='login')
def check_permissions(request):
    user = request.user
    user_groups = user.groups.all()
    user_permissions = user.get_all_permissions()

    logger.info(f"User: {user.username}")
    logger.info(f"User Groups: {[group.name for group in user_groups]}")
    logger.info(f"User Permissions: {user_permissions}")

    return HttpResponse("Check logs for user permissions info.")
