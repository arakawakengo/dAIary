from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Diary
from .serializers import DiarySerializer

import requests
import json
from django.http import HttpResponse

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

def TestGPT(request):
    url = 'http://localhost:8000/api/comment/'  # ローカル環境で動かしている場合
    data = {
        "context" : "あなたはトルコ人です。",
        "diary_text": "主食はなんですか"
        }  # ここに日記のテキストを入力

    response = requests.post(url, json=data)

    print(response.status_code)
    print(response.json())
    
    return HttpResponse(response.json()["response"])

