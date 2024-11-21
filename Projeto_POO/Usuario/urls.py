from django.urls import path
from django.http import HttpResponse
from Usuario.views import home, logout_user, register_user

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    
]
