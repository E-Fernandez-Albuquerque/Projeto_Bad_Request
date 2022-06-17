from django.urls import path, include

from chat.views import index
from chat.views import room

app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
