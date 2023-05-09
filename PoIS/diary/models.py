from django.db import models
from django.contrib.auth.models import User


class DiaryContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class DiaryComment(models.Model):
    commentID = models.IntegerField(primary_key=True)
    diaryId = models.ForeignKey()
    Select_Character_Role_ID = models.IntegerField()
    Select_Character_Disposition_ID = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
