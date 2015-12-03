"""movie_rec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView    #later we have to change it 


urlpatterns = [
    url(r'^$', 'predictions.views.home',name='home'),
    url(r'^user/$', 'predictions.views.user',name='user'),
	url(r'^movies/(?P<slug>[-\w]+)/$', 'predictions.views.movie_detail',name='movie_detail'),
	url(r'^movies/(?P<slug>[-\w]+)/edit/$', 'predictions.views.edit_movie',name='edit_movie'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
]










