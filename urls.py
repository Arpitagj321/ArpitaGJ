from django.urls import path
from django.contrib.auth.views import LoginView
from .views import signup_view, task_list, create_task, update_task, delete_task, logout_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='taskapp/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', task_list, name='task_list'),
    path('task/create/', create_task, name='create_task'),
    path('task/update/<int:task_id>/', update_task, name='update_task'),
    path('task/delete/<int:task_id>/', delete_task, name='delete_task'),
]
