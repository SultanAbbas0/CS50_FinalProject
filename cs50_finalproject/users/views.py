from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserProfileForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from notebook.models import Word
from django.http import JsonResponse


def Register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully!!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def Profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "User profile updated successfully!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)
    user = request.user
    words_number = Word.objects.filter(user=user).count()
    return render(request, 'users/profile.html', {'u_form':u_form, 'p_form':p_form, 'words_num':words_number})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
