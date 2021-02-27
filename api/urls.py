from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.shortcuts import redirect

from . import views

# namespacing app
app_name = 'api'

# API routes
urlpatterns = [

    url('ping/', views.PingView.as_view(), name='api-ping'),
    url('process/video', views.ProcessVideoView.as_view(), name='process-video'),
    path('', views.IndexView.as_view(), name='index'),
]