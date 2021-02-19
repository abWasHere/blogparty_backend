from django.shortcuts import render


def api_homepage(request):
    return render(request, 'config/home.html')
