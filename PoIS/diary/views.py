import json
import requests
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Diary, DiaryComment
from .serializers import DiarySerializer, DiaryCommentSerializer


# class DiaryListCreateView(generics.ListCreateAPIView):
#     queryset = Diary.objects.all()
#     serializer_class = DiarySerializer
#
#     # permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class DiaryView(APIView):
    serializer = DiarySerializer

    # permission_classes = [IsAuthenticated]　# 認証周りを擦り合わせる必要あり

    def get(self, request):
        diary_list = Diary.objects.all()
        # diary_list = Diary.objects.filter(user=user) # あとで自分のだけにする
        return Response(
            {
                "diary_list": [
                    {
                        "diary_id": diary.diary_id,
                        "user_id": diary.user.id,  # type: ignore
                        "title": diary.title,
                        "content": diary.content,
                        "created_at": diary.created_at,
                    }
                    for diary in diary_list
                ]
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = self.serializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            serializer.validated_data['user'] = user  # type: ignore
            diary = serializer.save()
            return Response(
                {
                    "diary_id": diary.diary_id,
                    "user_id": diary.user.id,
                    "title": diary.title,
                    "content": diary.content,
                    "created_at": diary.created_at,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def commentGenerate(data):

    url = 'http://localhost:8000/api/comment/'
    diary = Diary.objects.get(diary_id=data.get('diaryObject'))
    content = diary.content
    Select_Character_Role = data.get('Select_Character_Role')
    Select_Character_Disposition = data.get('Select_Character_Disposition')

    Message = {
        'content': content,
        'Select_Character_Role': Select_Character_Role,
        'Select_Character_Disposition': Select_Character_Disposition
    }

    response = requests.post(url, data=json.dumps(Message))

    return response.json()['detail']

class DiaryCommentView(APIView):
    serializer = DiaryCommentSerializer

    def get(self, request):
        diary_comment_list = DiaryComment.objects.all()
        return Response(
            {
                "diary_comment_list": [
                    {
                        'commentID': comment.commentID,
                        'diaryID': comment.diaryObject.diary_id,
                        'Select_Character_Role_ID': comment.Select_Character_Role,
                        'Select_Character_Disposition_ID': comment.Select_Character_Disposition,
                        'content': comment.content,
                        'created_at': comment.created_at
                    }
                    for comment in diary_comment_list
                ]
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        # 调用ChatGPT方法生成评论之后，序列化之后存储数据
        temp = request.data
        res = commentGenerate(temp)
        temp['content'] = res
        serializer = self.serializer(data=temp)
        if serializer.is_valid():
            comment = serializer.save()
            return Response(
                {
                    "commentID": comment.commentID,
                    "diaryID": comment.diaryObject.diary_id,
                    "Select_Character_Role": comment.Select_Character_Role,
                    "Select_Character_Disposition": comment.Select_Character_Disposition,
                    "content": comment.content,
                    "created_at": comment.created_at
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #    return Diary.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)


class DiaryByIDView(APIView):
    serializer = DiarySerializer

    # permission_classes = [IsAuthenticated]　# 認証周りを擦り合わせる必要あり

    def get(self, request, diary_id):
        diary = Diary.objects.get(diary_id=diary_id)
        return Response(
            {
                "diary_id": diary.diary_id,
                "user_id": diary.user.id,  # type: ignore
                "title": diary.title,
                "content": diary.content,
                "created_at": diary.created_at,
            },
            status=status.HTTP_200_OK
        )

    def delete(self, request, diary_id):
        Diary.objects.get(diary_id=diary_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
