from django.urls import path, include
from todos import views
from config import settings

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("post", views.todo_post, name="todo_post"),
]

if settings.DEBUG:
    urlpatterns += [
        path("debug/", include("debug_toolbar.urls")),
    ]
