from project_api.models import Project
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProjectSerializer, SnapshotSerializer, TagsSerializer
from .models import Project, Snapshot

# Create your views here.
@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def snapshot_detail(request, pk):
    snapshot = Snapshot.objects.get(id=pk)
    serializer = SnapshotSerializer(snapshot, many=False)
    return Response(serializer.data)