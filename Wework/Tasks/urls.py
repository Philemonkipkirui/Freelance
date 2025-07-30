from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path('task_info/', views.task_info, name='task_info'),
    path('ajax_filter_tasks/', views.ajax_filter_tasks, name='ajax_filter_tasks'),
    path('task_page/<int:task_id>/', views.task_page, name='task_page')

]