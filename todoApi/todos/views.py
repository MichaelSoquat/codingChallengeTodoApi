from django.shortcuts import render
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    def create(self, request):

        data = {
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'state': request.data.get('state'),
            'creation_date': request.data.get('creation_date'), 
            'priority': request.data.get('priority'), 
        }

        serializer = TaskSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

        else: 
            return Response(serializer.errors)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):

        task_to_edit = self.get_object()
        
        data = {
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'state': request.data.get('state'),
            'creation_date': request.data.get('creation_date'), 
            'priority': request.data.get('priority'), 
        }

        serializer = TaskSerializer(instance = task_to_edit, data = data)

        if serializer.is_valid():
            serializer.save()

        else: 
            return Response(serializer.errors)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        
        task_to_delete = self.get_object()
        task_to_delete.delete()

        return Response('Task deleted')