from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

def courses(request, *args, **kwargs):
    return render(request, 'courses/courses_list.html')