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
from django.views.generic import TemplateView, RedirectView    #later we have to change it 
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)
from predictions.backends import MyRegistrationView


urlpatterns = [
    url(r'^$', 'predictions.views.home',name='home'),
    url(r'^user/$', 'predictions.views.user',name='user'),
    url(r'^movies/$', RedirectView.as_view(pattern_name='browse')),
	url(r'^movies/(?P<slug>[-\w]+)/$', 'predictions.views.movie_detail',name='movie_detail'),
	url(r'^movies/(?P<slug>[-\w]+)/edit/$', 'predictions.views.edit_movie',name='edit_movie'),
    url(r'^browse/name/$', 'predictions.views.browse_by_name', name='browse'),
    url(r'^browse/name/(?P<initial>[-\w]+)/$', 'predictions.views.browse_by_name',name='browse_by_name'),
    url(r'^browse/$', RedirectView.as_view(
        pattern_name='browse')),
    url(r'^accounts/password/reset/$',password_reset,
        {'template_name':'registration/password_reset_form.html'},name="password_reset"),

    url(r'^accounts/password/reset/done/$',password_reset_done,
        {'template_name':'registration/password_reset_done.html'},name="password_reset_done"),

    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',password_reset_confirm,
        {'template_name':'registration/password_reset_confirm.html'},name="password_reset_confirm"),

    url(r'^accounts/password/done/$', password_reset_complete,
        {'template_name':'registration/password_reset_complete.html'},
        name="password_reset_complete"),

    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/create_movie/$', 'predictions.views.create_movie',name='registration_create_movie'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),

]















