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
    url('video/upload', views.UploadVideoView.as_view(), name='video-upload'),
    path('', views.IndexView.as_view(), name='index'),
]