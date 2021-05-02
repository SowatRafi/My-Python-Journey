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

    print(request.POST['text'])
    return redirect('index')