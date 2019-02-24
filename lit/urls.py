from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^essays/$', views.essays, name='essays'),
        url(r'^story_list/$', views.story_list, name='story_list'),
        url(r'^story_detail/(?P<pk>\d+)/$', views.story_detail, name='story_detail'),
        #pk = primary key for the story number
        url(r'^poem_list/$', views.poem_list, name='poem_list'),
        url(r'^poem_detail/(?P<pk>\d+)/$', views.poem_detail, name='poem_detail'),
]
