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
    url('video/upload/', views.UploadVideoView.as_view(), name='video-upload'),
    url('processed/info/', views.ProcessedVideosView.as_view(), name='processed-videos-all'),
    url('processed/', views.ProcessedVideoView.as_view(), name='processed-video'),
    path('', views.IndexView.as_view(), name='index'),
]