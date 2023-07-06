
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('todos', views.todo_list),
    path('todos/<int:pk>',views.todo_detail)
]

urlpatterns += staticfiles_urlpatterns()
