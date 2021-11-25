from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserForm, NameForm, Contactus
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are registered successfully!')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = Contactus(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            subject = 'Someone contacted us.'
            content = f"""
            {first_name} {last_name} is trying to contact you.
            Their email address os {email}
            Message: {message}
            """

            send_mail(subject=subject, message=content, from_email='sometestemaill123@gmail.com',
                      recipient_list=['sometestemaill123@gmail.com'])
            return redirect('thank_you')
    else:
        form = Contactus()

    return render(request, 'users/contact_us.html', {'form': form})


def thank_you(request):
    return render(request, 'users/thank_you.html')
