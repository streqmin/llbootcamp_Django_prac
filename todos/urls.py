from django.urls import path, include
from todos import views
from config import settings

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("post/", views.todo_post, name="todo_post"),
    # http://127.0.0.1:8000/todo?number=1&name=ghldkf
    # http://127.0.0.1:8000/todo/{1}/ + GET, POST, PUT, DELETE, OPTION
    path("<int:pk>", views.todo_detail, name="todo_detail"),
    path("<int:pk>/edit", views.todo_edit, name="todo_edit"),
    path("<int:pk>/done", views.todo_done, name="todo_done"),
    path("done_list/", views.done_list, name="done_list"),
    # path("drf/", views.todo_drf, name="todo_drf"),
    path("drf/", views.TodoAPIView.as_view(), name="todo_drf"),
]

if settings.DEBUG:
    urlpatterns += [
        path("debug/", include("debug_toolbar.urls")),
    ]
