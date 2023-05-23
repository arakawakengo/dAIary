from django.urls import path
from .views import DiaryByIDView,  DiaryCommentView, DiaryView
from . import views

urlpatterns = [
    path('diaries/', DiaryView.as_view()),
    path('diaries/<int:diary_id>/', DiaryByIDView.as_view()),
    path('diaries/CommentView/<int:diary_id>/', DiaryCommentView.as_view()),
]
