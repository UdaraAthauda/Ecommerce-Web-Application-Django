from django.shortcuts import render


# index/home view
def index(request):
    return render(request, 'index.html')