from django.shortcuts import render


def home(request):
    return render(request, 'knowledge/home.html')

def about(request):
    return render(request, 'knowledge/about.html')