import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'homepage/post_list.html', {'posts': posts})

""" teapot

def index(request):
	 r = requests.get("http://httpbin.org/status/418")
	 print(r.text)
	 return HttpResponse("<pre>" + r.text + "</pre>")

"""
