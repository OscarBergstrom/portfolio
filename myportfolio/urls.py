from django.shortcuts import render

def works_view(request):
    return render(request, 'portfolio/home.html')
