from django.shortcuts import render
from .models import Course
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    course = Course.objects.all;
    return render(request, 'courses.html',{'courses' : course})