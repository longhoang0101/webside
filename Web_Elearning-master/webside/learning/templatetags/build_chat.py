from django import template
from django.urls import reverse_lazy as reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
register = template.Library()


@register.simple_tag
def build_chat_room_name(username1, username2):
    return '-'.join(sorted([username2 ,username1]))


@register.simple_tag
def build_chat_url(username):
    user = User.objects.filter(username = username).filter(groups__name='NormalCustomer')
    if user.exists():
        return reverse('chat', kwargs={
            'chatname': build_chat_room_name("idragon1st",username )})
    else:
        return "/chat"


@register.simple_tag
def check_user_permission(username):
    user = User.objects.filter(username = username).filter(groups__name='Instructor')
    if user.exists():
        return True
    else:
        return False
