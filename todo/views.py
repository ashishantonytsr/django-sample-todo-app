from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Todo
from .forms import TodoModelForm


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todos" : todos
    }
    return render(request, "todo/list.html", context)

def todo_create(request):
    form = TodoModelForm()
    if request.method == "POST":
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form" : TodoModelForm()
    }
    return render(request, "todo/create.html", context)

def todo_detail(request, pk):
    todo = Todo.objects.get(id = pk)
    context = {
        "todo": todo
    }
    return render(request, "todo/detail.html", context)

def todo_update(request, pk):
    todo = Todo.objects.get(id = pk)
    form = TodoModelForm(instance=todo)
    if request.method == "POST":
        form = TodoModelForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('../')
    context = {
        'form': form,
        'todo': todo
    }
    return render(request, "todo/update.html", context)

def todo_delete(request, pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return redirect('/')

class TodoListView(generic.ListView):
    template_name = 'todo/list.html'
    queryset = Todo.objects.all()
    context_object_name = 'todos'

class TodoCreateView(generic.CreateView):
    template_name = 'todo/create.html'
    form_class = TodoModelForm

    def get_success_url(self):
        return reverse('todo:todo-list')
    
class TodoDetailView(generic.DetailView):
    template_name = 'todo/detail.html'
    queryset = Todo.objects.all()
    context_object_name = 'todo'

class TodoUpdateView(generic.UpdateView):
    template_name = 'todo/update.html'
    queryset = Todo.objects.all()
    form_class = TodoModelForm

    def get_success_url(self):
        return "../"

class TodoDeleteView(generic.DeleteView):
    template_name = 'todo/delete.html'
    queryset = Todo.objects.all()

    def get_success_url(self):
        return reverse('todo:todo-list')