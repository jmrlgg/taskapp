from rest_framework.response import Response
# Model USE
from .models import TaskModel
# Import Serializer
from .serializers import TaskModelSerializer
from django.http import HttpResponse

# Return Task List
def getTaskList(request):
    # Get Task List
    taskList = TaskModel.objects.all()
    # Serialize Task List
    serializer = TaskModelSerializer(taskList, many=True)
    # Return Task List
    return HttpResponse(serializer.data)

#IMPORT JSON
import json
# Return     Task Detail
def getTaskDetail(request):
    # Get Task Detail
    taskDetail = TaskModel.objects.all()
    
    # Serialize Task Detail
    serializer = TaskModelSerializer(taskDetail, many=True)
    # Return Task Detail JSON Serializer
    serializer_data = serializer.data
    json_data = json.dumps(serializer_data) 
    return Response(serializer.data)


#  Create Task
def createTask(request):
    # Get Task Data
    taskData = request.data
    # Serialize Task Data
    serializer = TaskModelSerializer(data=taskData)
    # Return Task Data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)