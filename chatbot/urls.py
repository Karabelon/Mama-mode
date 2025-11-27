from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot, name="chatbot"),
    path('send_chat_message/', views.send_chat_message, name='send_chat_message'),
]

