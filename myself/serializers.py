from rest_framework import serializers
from .models import Myself

class MyselfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myself
        fields = '__all__'