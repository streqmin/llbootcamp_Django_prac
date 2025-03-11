from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


def home(request):
    return render(request, "home.html")


def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, "todo_list.html", {"todos": todos})


def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.isValid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todo_post.html", {"form": form})


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, "todo_detail.html", {"todo": todo})
