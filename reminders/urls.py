from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminders, name='reminders'),
    path('delete/<int:id>/', views.delete_reminder, name='delete_reminder'),
]

