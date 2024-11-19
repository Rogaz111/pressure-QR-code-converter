from django.http import HttpResponse
from django.shortcuts import render


# Home Page Route
def home(request):
    return render(request, "my_app/home.html")


# CSV Import Route
def import_view(request):
    return render(request, "my_app/imports.html")