from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'main.html', {})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
