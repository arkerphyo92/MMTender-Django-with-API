from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import RegisterForm, UserGroupForm
from django.contrib.auth.models import User, Group
from .forms import UserGroupForm, UserGroupAssignmentForm
from django.core.paginator import Paginator

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after successful registration
            return redirect('listings:tenders')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('frontend:index')
    return redirect('frontend:index')

def select_username(request):
    if request.method == 'POST':
        username_id = request.POST.get('username_id')
        return redirect('users:assign_group_id', user_id=username_id)

    usernames = User.objects.filter(is_superuser=False)
    return render(request, 'users/username_list.html', {
        'usernames': usernames,
    })

def assign_group(request):
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            selected_groups = request.POST.getlist('groups')
            user.groups.clear()
            user.groups.add(*selected_groups)
            return redirect('users:users')
    else:
        form = UserGroupForm()

    usernames = User.objects.filter(is_superuser=False)
    allgroups = Group.objects.all()

    # Check if the current user is a superuser
    is_superuser = request.user.is_superuser

    return render(request, 'users/assign_group.html', {
        'form': form,
        'usernames': usernames,
        'allgroups': allgroups,
        'is_superuser': is_superuser,
    })

def assign_group_id(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    allgroups = Group.objects.all()
    
    if request.method == 'POST':
        group_ids = request.POST.getlist('groups')
        user.groups.set(group_ids)
        return redirect('users:users')
    
    return render(request, 'users/assign_group_id.html', {
        'user': user,
        'allgroups': allgroups
    })





def users(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)  # Show 10 tenders per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/users.html', {'page_obj': page_obj})

