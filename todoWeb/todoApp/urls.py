from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTask, name='add'),
    path('complete/<todo_id>', views.completeTask, name='complete'),
    path('delete/<todo_id>', views.deleteTask, name='delete'),
    path('api', views.TodoList.as_view(), name='api'),
    path('o', include('oauth2_provider.urls', namespace='o')),
]