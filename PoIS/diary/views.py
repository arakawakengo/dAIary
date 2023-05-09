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


    def get (self,request):
        user = request.user
        diary_list = Diary.objects.all() # あとで自分のだけにする
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]
    
    #def get_queryset(self):
    #    return Diary.objects.filter(user=self.request.user)

    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

