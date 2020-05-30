"""webside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

#Add Django site authentication urls (for login, logout, password management)
from chat.views import ChatView, MessagesAPIView

urlpatterns = [
    path("", include("learning.urls")),
    path("flights", include("flights.urls")),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/<slug:chatname>/', ChatView.as_view(), name='chat'),
    path('api/messages/<slug:chatname>/', MessagesAPIView.as_view(), name="messages"),
]

