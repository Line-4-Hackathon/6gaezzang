from django.shortcuts import render
from django.views.generic import DetailView
from user.models import Fuser

# Create your views here.
"""
def mypage(request):
    return render(request, 'mypage.html')"""

def developer(request):
    return render(request, 'developer.html')

def course(request):
    return render(request, 'course.html')

def course2(request):
    return render(request, 'course2.html')

def mountation(request):
    return render(request, 'mountation.html')

def weather(request):
    return render(request, 'weather.html')

def loading(request):
    return render(request, 'loading.html')

class MemberDetailView(DetailView): 
    template_name = 'mypage.html' 
    model = Fuser
