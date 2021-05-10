from rest_framework import serializers
from .models import Project, Snapshot, Tags

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'finished', 'description', 'demo_url', 'github_url', 'created_at', 'updated_at', 'header_image', 'user', 'tags', 'snapshots']

class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'