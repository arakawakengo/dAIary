from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at')
