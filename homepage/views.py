import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
	return render(request, 'homepage/post_list.html', {})

""" teapot

def index(request):
	 r = requests.get("http://httpbin.org/status/418")
	 print(r.text)
	 return HttpResponse("<pre>" + r.text + "</pre>")

"""