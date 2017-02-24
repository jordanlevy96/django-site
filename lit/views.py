import requests
from django.shortcuts import render

# Create your views here.
def essays(request):
	return render(request, 'lit/essays.html')