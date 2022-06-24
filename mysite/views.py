from django.shortcuts import render, redirect
from .form import *
from .models import *
from mysite.models import *


# home page
def index(request):
    return render(request, 'index.html')

# comment fun
def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            form.save()
            return redirect("django:form")
    else:
        form = Login()

    context = {
        "form": form,
        "homes": My.objects.all(),
    }

    return render(request, "form.html", context)

# add chart fun

def addchart(request):
    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return redirect("django:chart")
    else:
        form = User()

    context = {
        "form": form,
        "homes": Down.objects.all(),
    }
    return render(request, "chartSignUp.html", context)

# chart fun
def chart(request):
    context = {
        "homes":Down.objects.all()
    }
    return render(request, "chart.html", context)
