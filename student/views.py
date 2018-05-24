from django.shortcuts import render

# Create your views here.
rom .models import Student

# Create your views here.

def home(request):
	return render(request,'base.html')
