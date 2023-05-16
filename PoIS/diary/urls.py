from django.urls import path
from .views import DiaryByIDView,  DiaryCommentView, DiaryView

urlpatterns = [
    path('diaries/', DiaryView.as_view()),
    path('diaries/<int:diary_id>', DiaryByIDView.as_view()),
    path('diaries/CommentView', DiaryCommentView.as_view()),
]
