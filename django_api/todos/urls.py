from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoAPI.as_view()),
]