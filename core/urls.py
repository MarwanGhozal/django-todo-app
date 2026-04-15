from django.urls import path
from .views import (
    HomePage,
    TaskList, TaskDetail, TaskCreate,
    TaskUpdate, TaskDelete,
    CustomLoginView, RegisterPage,
    task_toggle
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # 🌍 Public homepage
    path('', HomePage.as_view(), name='home'),

    # 🔐 Auth
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # 📌 App (protected)
    path('tasks/', TaskList.as_view(), name='taskList'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),

    path('task/<int:pk>/toggle/', task_toggle, name='task-toggle'),
]