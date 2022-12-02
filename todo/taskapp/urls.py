from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homeview"),
    path("task/<pk>", views.TaskView.as_view(), name="taskview"),
]