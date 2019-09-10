from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_condition import Or
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication
from django_filters import rest_framework as filters
from .models import Todo
from .serializers import ToDoSerializer
from .forms import TodoForm
from datetime import datetime
# Def Index criada para redirecionar as queries dos models para o template ter acesso.
def index(request):
    task = Todo.objects.order_by('id')
    form = TodoForm()
    context={'task': task, 'form' : form}
    return render(request,'todoApp/index.html', context)

@require_POST
def addTask(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        newTask = Todo(title=request.POST['title'],desc=request.POST['desc'], deadline=request.POST['deadline'])
        newTask.save()
        
    return redirect('index')

def completeTask(request, todo_id):
    task = Todo.objects.get(pk=todo_id)
    task.complete = True
    task.completed_at = datetime.now()
    task.save()
    return redirect('index')

def deleteTask(request, todo_id):
    task = Todo.objects.get(pk=todo_id)
    task.delete()
    return redirect('index')

# classe das APIs.
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = ToDoSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'