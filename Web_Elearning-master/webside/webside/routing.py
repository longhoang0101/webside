from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path

from chat.consumers import ChatConsumer


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            #re_path(r'chat//<slug:chatname>/', ChatConsumer),
            path('chat/<slug:chatname>/', ChatConsumer),
        ])
    ),
})
