import requests
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Story
from .models import Poem

# Create your views here.
def essays(request):
	return render(request, 'lit/essays.html')

def story_list(request):
    stories = Story.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lit/story_list.html', {'story_list': stories})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'lit/story_detail.html', {'story': story})

def poem_list(request):
    poems = Poem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lit/poem_list.html', {'poem_list': poems})

def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    return render(request, 'lit/poem_detail.html', {'poem': poem})