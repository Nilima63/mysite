from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # Add this line

def home(request):  # Add this function
    return HttpResponse("Welcome to mysite!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Add this line to handle the root URL
]
