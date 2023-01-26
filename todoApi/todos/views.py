from rest_framework.response import Response
from .models import Task
from .serializers import RegisterSerializer, TaskSerializer, UserSerializer
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action




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
            'creator': request.data.get('creator') if request.data.get('creator') else ''
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
            'creator': request.data.get('creator') if request.data.get('creator') else ''
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


class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @action(detail = False, methods = ['post'])
    def register(self, request):

        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        data = UserSerializer(user).data

        return Response(data, status = status.HTTP_201_CREATED)