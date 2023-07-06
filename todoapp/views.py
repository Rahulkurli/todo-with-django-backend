from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodoSerializer

@api_view(["GET","POST"])
def todo_list(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(["GET", "PUT", "PATCH", "DELETE"])
def todo_detail(request,pk):
    todo = get_object_or_404(Todo, id=pk)

    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


    elif request.method == "PUT":
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PATCH":
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
