from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<int:id>/',views.delete_task, name='delete_task'),
    path('edit/<int:id>/',views.edit_task, name='edit_task'),
    path('complete/<int:id>/',views.complete_task, name='complete_task'),
    path('pending/<int:id>/',views.pending_task, name='pending_task'),
]