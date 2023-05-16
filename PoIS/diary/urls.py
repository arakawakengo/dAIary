from django.urls import path
from .views import DiaryListCreateView, DiaryRetrieveUpdateDestroyView, DiaryCommentView
from . import views

urlpatterns = [
    path('diaries/', DiaryListCreateView.as_view(), name='diary_list_create'),
    path('diaries/<int:pk>/', DiaryRetrieveUpdateDestroyView.as_view(), name='diary_retrieve_update_destroy'),
    path('diaries', DiaryCommentView.as_view(), name='diart_comment_view'),
    path("gpt_test/", views.TestGPT, name="index"),
]
