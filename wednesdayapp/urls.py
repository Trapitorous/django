from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('detail/<int:id>/', views.task_detail, name='task_list'),
    path('create/', views.create_task, name='task_list'),
    path('update/<int:id>/', views.edit_task, name='task_list'),
    path('delete/<int:id>/', views.delete_task, name='task_list'),
]
