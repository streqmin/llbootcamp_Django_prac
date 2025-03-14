from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .serializers import TodoSerializer


def home(request):
    return render(request, "home.html")


def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, "todo_list.html", {"todos": todos})


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, "todo_detail.html", {"todo": todo})


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


def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            # SQL 실행시킨 상태이지만 = 메모리에만 올려놓고 영구저장(commit)은 안한상태
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)  # 레코드,튜플 #

    return render(request, "todo_post.html", {"form": form})


def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect("todo_list")


def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, "todo_done.html", {"dones": dones})


# @api_view(["GET"])
# def todo_drf(request):
#     return Response({"message": "Hello World!"})


# def todo_drf(request):
#     return JsonResponse({"message": "Hello World!"})


class TodoAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
