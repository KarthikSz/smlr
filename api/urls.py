from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.shortcuts import redirect

from . import views

# namespacing app
app_name = 'api'

urlpatterns = [

    # User-auth routes
    path('', views.IndexView.as_view(), name='index'),
    url('ping/', views.PingView.as_view(), name='api-ping'),
]