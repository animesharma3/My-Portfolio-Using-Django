from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyselfSerializer
from .models import Myself
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
def profile_detail(request):
    user = User.objects.get(id=1)
    myself = user.myself
    serializer = MyselfSerializer(myself, many=False)
    return Response(serializer.data)