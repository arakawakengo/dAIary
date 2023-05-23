from django.db import models
from django.contrib.auth.models import User


class Diary(models.Model):
    diary_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.diary_id)




class DiaryComment(models.Model):
    commentID = models.AutoField(primary_key=True)
    diaryObject = models.ForeignKey(Diary, on_delete=models.CASCADE)
    Select_Character_Role = models.IntegerField()
    Select_Character_Disposition = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
