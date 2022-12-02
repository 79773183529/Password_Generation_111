from django.shortcuts import render
from django.http import HttpResponse
import string
import random
from .with_files import add_password


# Create your views here.
def home(request):
    return render(request, 'Generator/home.html')


def password(request):
    the_password = ''
    letters = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        letters.extend(string.ascii_uppercase)
    if request.GET.get('numbers'):
        letters.extend(string.digits)
    if request.GET.get('special'):
        letters.extend('.,-_?!$@=+')
    length = request.GET.get('length', 13)
    for _ in range(int(length)):
        chair = random.choice(letters)
        the_password += chair
    login = request.GET.get('login', 'login')
    site_name = request.GET.get('site_name', 'site_name')
    add_password(site_name=site_name, login=login, password=the_password)

    return render(request, 'Generator/password.html', {'password': the_password})


def columbia(request):
    return render(request, 'Generator/trash.html')




