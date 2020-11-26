from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    # return HttpResponse("About Page")
    return render(request, "aboutpage.html")


def home(request):
    # return HttpResponse("home Page")
    return render(request, "homepage.html")
