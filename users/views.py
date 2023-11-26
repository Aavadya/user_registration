

from django.shortcuts import render, redirect
from .forms import PatientSignUpForm, DoctorSignUpForm,LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username)
            if user.password == password:
                print(user)
                if user is not None:
                    
                    if user.user_type == 'patient':
                        return redirect('patient_dashboard')
                    elif user.user_type == 'doctor':
                        return redirect('doctor_dashboard')
                else:
                    messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form})



def patient_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.user_type == 'patient':
                login(request, user)
                return redirect('patient_dashboard')
            else:
                messages.error(request, 'Invalid username or password for patient.')
    else:
        form = LoginForm()
    return render(request, 'patient_login.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.user_type == 'doctor':
                login(request, user)
                return redirect('doctor_dashboard')
            else:
                messages.error(request, 'Invalid username or password for doctor.')
    else:
        form = LoginForm()
    return render(request, 'doctor_login.html', {'form': form})

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render( request, 'index.html')
    else:
        form = PatientSignUpForm()
    return render(request, 'patient_signup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = DoctorSignUpForm()
    return render(request, 'doctor_signup.html', {'form': form})
