from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Diary
from .serializers import DiarySerializer

class DiaryListCreateView(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    # permission_classes = [IsAuthenticated]
   
    def perform_create(self, serializer):             
        serializer.save(user=self.request.user)


class DiaryView(APIView):
    serializer = DiarySerializer
    # permission_classes = [IsAuthenticated]　# 認証周りを擦り合わせる必要あり

    def get (self,request):
        user = request.user
        diary_list = Diary.objects.all()
        # diary_list = Diary.objects.filter(user=user) # あとで自分のだけにする
        return Response(
            {
                "diary_list": [
                    {
                        "diary_id": diary.diary_id,
                        "user_id":  diary.user.id,
                        "title":  diary.title,
                        "content":  diary.content,
                        "created_at":  diary.created_at,
                    }
                    for diary in diary_list
                ]
            },
            status=status.HTTP_200_OK
        )

    
    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            diary = serializer.save()
            return Response(
                {
                    "diary_id":     diary.diary_id,
                    "user_id":      diary.user.id,
                    "title":        diary.title,
                    "content":      diary.content,
                    "created_at":   diary.created_at,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]
    
    #def get_queryset(self):
    #    return Diary.objects.filter(user=self.request.user)

    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)


class DiaryByIDView(APIView):
    serializer = DiarySerializer
    # permission_classes = [IsAuthenticated]　# 認証周りを擦り合わせる必要あり

    def get(self, request, diary_id):
        diary = Diary.objects.get(diary_id=diary_id)
        return Response(
                {
                    "diary_id":     diary.diary_id,
                    "user_id":      diary.user.id,
                    "title":        diary.title,
                    "content":      diary.content,
                    "created_at":   diary.created_at,
                },
                status=status.HTTP_200_OK
            )
    
    def delete(self, request, diary_id):
        Diary.objects.get(diary_id=diary_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
