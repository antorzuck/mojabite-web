from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def view_item(request):
    return render(request, 'view.html')