from django.shortcuts import render


def index(request):
    return render(request, "base/index.html")


def homepage(request):
     return render(request, "base/homepage.html")

