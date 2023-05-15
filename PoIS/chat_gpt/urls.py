from django.urls import path
from .views import ChatGPTView

urlpatterns = [
    path('', ChatGPTView.as_view(), name='gpt3.5'),
]
