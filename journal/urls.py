from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal, name='journal'),
    path('delete/<int:id>/', views.delete_entry, name='delete_entry'),  # new
]

