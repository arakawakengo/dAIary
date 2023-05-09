from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import DiaryContent, DiaryComment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import DiarySerializer


class DiaryListCreateView(generics.ListCreateAPIView):
    queryset = DiaryContent.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DiaryCommentView(APIView):
    queryset = DiaryComment.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        content = self.queryset.get('content')
        return Response(content)


class DiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiaryContent.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #    return Diary.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)
