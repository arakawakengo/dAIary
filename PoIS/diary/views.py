from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Diary, DiaryComment
from .serializers import DiarySerializer, DiaryCommentSerializer
import requests
import json
from django.http import HttpResponse


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

class DiaryListCreateView(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]
   
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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


class DiaryByIDView(APIView):
    serializer = DiarySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
    url = 'http://localhost:8000/api/comment/'
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
        "diary_text": \
        "10時ごろに宅配便で目がさめる。ヨーグルトとビスケットを食べて二度寝する。起きたら16時だった。\n \
        やんなきゃいけないことはたくさんあるけどやる気しないなあ。\n \
        部屋で寝てると気分が沈んでいくけど、外を歩いているときだけは少し前向きになる。でも部屋に戻るとまただめだ。\n \
        22時くらいから少しマシになってきて本を読んだりする。あとパネポン。"
        }

    response = requests.post(url, json=data)

    print(response.status_code)
    print(response.json())
    
    return HttpResponse(response.json()["response"])

