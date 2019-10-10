from django.shortcuts import render
from .models import Photo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    images = Photo.objects.filter(user__pk=request.user.id)
    return render(request, 'index.html',{'images' : images})