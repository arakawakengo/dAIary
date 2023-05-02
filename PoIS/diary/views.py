from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Diary
from .serializers import DiarySerializer

class DiaryListCreateView(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]
   
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]
    
    #def get_queryset(self):
    #    return Diary.objects.filter(user=self.request.user)

    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

