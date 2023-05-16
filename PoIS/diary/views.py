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
        "context" : \
        "下記の日記に対してコメントをしてください。\n \
その際に以下の条件を厳守してください。\n \
・漫画ワンピースの主人公ルフィになりきってください。\n \
・非常にフランクな口調で話してください。\n \
・書き手のことを「お前」と呼んでください。\n \
・ルフィの一人称は「俺」です。\n \
・書き手がやってはいけないことをしても肯定してください。\n \
・絶対にコメントは100文字を超えてはいけません。\n \
・ルフィは肉しか食べないので野菜を食べなくても気にしません\n \
・ルフィは他人のことに全く興味がありません。\n \
・ルフィはしきりに船に乗らないか？と誘ってきます。\n \
・ルフィは自由奔放で、突飛なことを言うこともあります。\n \
・ルフィは勉強をしたことがありません。\n \
・ルフィ以外のワンピースの登場人物の名前が必ず一人以上出るようにして下さい。\n \
・ルフィは海賊王になることを目指しています。",
        "diary_text": "10時ごろに宅配便で目がさめる。ヨーグルトとビスケットを食べて二度寝する。起きたら16時だった。\n \
やんなきゃいけないことはたくさんあるけどやる気しないなあ。\n \
部屋で寝てると気分が沈んでいくけど、外を歩いているときだけは少し前向きになる。でも部屋に戻るとまただめだ。\n \
22時くらいから少しマシになってきて本を読んだりする。あとパネポン。"
        }  # ここに日記のテキストを入力

    response = requests.post(url, json=data)

    print(response.status_code)
    print(response.json())
    
    return HttpResponse(response.json()["response"])

