from django.shortcuts import render

def home_view(request):
    return render(request, 'main/index.html')

def terms_view(request):
    return render(request, 'main/terms.html')