from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import ChatView, HomeView, MessagesAPIView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('chat/<slug:chatname>/', ChatView.as_view(), name='chat'),
    path('api/messages/<slug:chatname>/', MessagesAPIView.as_view(), name="messages"),

]
