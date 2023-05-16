from django.urls import path
from .views import DiaryView, DiaryByIDView

urlpatterns = [
    path('diaries/', DiaryView.as_view()),
    path('diaries/<int:diary_id>', DiaryByIDView.as_view())
]