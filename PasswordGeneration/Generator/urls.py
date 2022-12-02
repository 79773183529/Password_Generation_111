from django.urls import path, include
from .views import home, password, columbia

urlpatterns = [
    path('', home, name='home'),
    path('password/', password, name='pass'),
    path('columbia/', columbia, name='columbia'),
]
