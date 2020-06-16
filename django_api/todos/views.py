from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Todo

# Create your views here.

class TodoAPI(APIView):
    def get(self, request):
        user = request.user
        todos = Todo.objects.filter(owner=user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
        
    # def post(self, request):
        # pass

# class TodoDetailAPI(APIView):
#     def put(self, request, todo_pk):
#         pass

#     def delete(self, request, todo_pk):
#         pass
        