from django.shortcuts import render

# Create your views here ACCOUNTS.
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')