from rest_framework import serializers
from .models import Diary, DiaryComment


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('title', 'content', 'created_at')


class DiaryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryComment
        fields = ('Select_Character_Role','Select_Character_Disposition', 'content', 'created_at')
