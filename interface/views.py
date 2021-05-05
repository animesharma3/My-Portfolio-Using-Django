from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    myself = User.objects.get(id=1).myself
    return render(request, 'index.html', context={'myself': myself})