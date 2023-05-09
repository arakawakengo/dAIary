from django.urls import path
from .views import DiaryListCreateView, DiaryRetrieveUpdateDestroyView, DiaryView

urlpatterns = [
    # path('diaries/', DiaryListCreateView.as_view(), name='diary_list_create'),
    path('diaries/', DiaryView.as_view()),
    path('diaries/<int:pk>/', DiaryRetrieveUpdateDestroyView.as_view(), name='diary_retrieve_update_destroy'),
]
