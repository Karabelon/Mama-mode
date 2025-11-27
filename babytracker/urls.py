from django.urls import path
from . import views

urlpatterns = [
    path("", views.babytracker, name="babytracker"),
    path("delete/<int:id>/", views.delete_activity, name="delete_activity"),
]


