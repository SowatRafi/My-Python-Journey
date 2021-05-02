from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ToDoListForm
from django.views.decorators.http import require_POST


# Create your views here.

def index(request):
    todo_items = ToDoList.objects.order_by('id')
    form = ToDoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, "ToDoList_APP/index.html", context)


@require_POST
def addTodoItem(request):
    form = ToDoListForm(request.POST)
    if form.is_valid():
        new_todo = ToDoList(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completedTodo(request, todo_id):
    todo = ToDoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    ToDoList.objects.filter(completed__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    ToDoList.objects.all().delete()

    return redirect('index')
