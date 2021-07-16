from django.urls import path
from .views import (
    TodoListView,
    TodoCreateView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView
) 
    

app_name = "todo"

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
]
