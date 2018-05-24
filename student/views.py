from django.shortcuts import render

# Create your views here.
from .models import Student

# Create your views here.

def home(request):
	return render(request,'base.html')
