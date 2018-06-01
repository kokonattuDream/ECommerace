from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        "title": "hello world"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    return render(request, "home_page.html", {})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        "title": "Contact",
        "content":"Welcome to the contact page",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    
    context = {
        "form": form
    }
    
    if form.is_valid():
        print(form.cleaned_data)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            return redirect("/")
        else:
            print("Error")
   

    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)

    return render(request, "auth/register.html", {})