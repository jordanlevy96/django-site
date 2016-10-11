import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'homepage/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'homepage/post_detail.html', {'post': post})

""" teapot

def index(request):
	 r = requests.get("http://httpbin.org/status/418")
	 print(r.text)
	 return HttpResponse("<pre>" + r.text + "</pre>")

"""
