from django.shortcuts import render, HttpResponse

# Create your views here TODO.

def get_todo_list(request):
    return render(request, "todo_list.html")
    
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')