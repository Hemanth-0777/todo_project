from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]