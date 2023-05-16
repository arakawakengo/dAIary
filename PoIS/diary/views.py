from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Diary
from .serializers import DiarySerializer

import requests
import json
from django.http import HttpResponse


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
                        "user_id":  diary.user.id, # type: ignore
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
    

class DiaryByIDView(APIView):
    serializer = DiarySerializer
    # permission_classes = [IsAuthenticated]　# 認証周りを擦り合わせる必要あり

    def get(self, request, diary_id):
        diary = Diary.objects.get(diary_id=diary_id)
        return Response(
                {
                    "diary_id":     diary.diary_id,
                    "user_id":      diary.user.id, # type: ignore
                    "title":        diary.title,
                    "content":      diary.content,
                    "created_at":   diary.created_at,
                },
                status=status.HTTP_200_OK
            )
    
    def delete(self, request, diary_id):
        Diary.objects.get(diary_id=diary_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

