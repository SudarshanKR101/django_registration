# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from register.models import Registration
from register.forms import RegistrationForm

def registration_list(request):
    users = Registration.objects.all()
    return render(request, 'register/list.html', {'users': users})

def registration_create(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm()
    return render(request, 'register/form.html', {'form': form})

def registration_update(request, pk):
    user = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm(instance=user)
    return render(request, 'register/form.html', {'form': form})

def registration_delete(request, pk):
    user = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('registration_list')
    return render(request, 'register/confirmation_delete.html', {'user': user})