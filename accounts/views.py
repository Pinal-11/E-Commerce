from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['name'] = username
            return redirect('/')

        else:
            messages.info(request, 'Oops!!! Invalid Credentials please register yourself...')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                user.save();
                return redirect('login')

        else:
            messages.info(request, 'password not matching!!!!!')
            return redirect('register')
        return redirect('/t')

    else:
        return render(request, "accounts/register.html")
