from rest_framework import serializers
from .models import Diary, DiaryComment


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at')


class DiaryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryComment
        fields = ('commentID', 'diaryID', 'Select_Character_Role',
                  'Select_Character_Disposition', 'content', 'created_at'
                  )
