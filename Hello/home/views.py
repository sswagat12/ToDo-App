from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from home.models import ContactUs, ToDo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from home.forms import ToDoForm

"""Home Page---->Redirecting unauthenticated users to login page, only authenticated users can go to index(home page)"""
"""API to fetch ToDO entry"""


def index(request):

    if request.user.is_anonymous:
        return redirect("/login")
    form = ToDoForm
    user = request.user
    toDo_all = ToDo.objects.filter(user=user).order_by('priority')
    return render(request, "index.html", context={'form': form, 'toDo_all': toDo_all})


"""API to create ToDo entry"""


def add_toDo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = ToDoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            toDo = form.save(commit=False)
            # print(toDo)
            toDo.user = user
            toDo.save()
            print(toDo)
            return redirect("/")
        else:
            return render(request, 'index.html', context={'form': form})


"""API to delete ToDo entry"""


def delete_toDo(request, id):
    ToDo.objects.get(pk=id).delete()
    return redirect('/')


"""API to update status of ToDo"""


def update_status_toDo(request, id, status):
    toDo = ToDo.objects.get(pk=id)
    toDo.status = status
    toDo.save()
    return redirect("/")


"""User Authentication APIs"""


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = authenticate(username=username, password=password1)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "You have logged in successfully")
            return redirect("/")
        else:
            messages.error(request, "Please enter the correct credentials")
            return render(request, 'login.html')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    messages.success(request, "Successfully logged out. C ya soon!!")
    return redirect("/login")


def signUp(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        confirmPassword = request.POST['confirmPassword']

        # Validating the inputs
        if len(username) > 15:
            messages.error(request, "Username must be within 10 characters")
            return render(request, 'signUp.html')
        if not username.isalnum:
            messages.error(
                request, "Username should only contain letters and numbers")
            return render(request, 'signUp.html')
        if password1 != confirmPassword:
            messages.error(
                request, "Passwords don't match. Please make sure password and confirm password are similar")
            return render(request, 'signUp.html')

        # Registering the user
        myUser = User.objects.create_user(username, email, password1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.phoneNumber = phoneNumber
        myUser.save()
        messages.success(request, "Your account is created successfully")
        return redirect('/')
    return render(request, "signUp.html")


"""************"""


"""Cantact Us API to retrieve user details"""


def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        queryIfAny = request.POST.get('queryIfAny')

        contact = ContactUs(name=name, email=email, phone=phone,
                            queryIfAny=queryIfAny, date=datetime.today())
        contact.save()
        messages.success(
            request, "Details uploaded successfully, we will reach out to you soon.")

    return render(request, "contactUs.html")
