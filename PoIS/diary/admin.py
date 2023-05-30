from django.contrib import admin

# モデルをインポート
from . models import Diary, DiaryComment

class DiaryAdmin(admin.ModelAdmin):
    list_display = ['title']


# 管理ツールに登録
admin.site.register(Diary, DiaryAdmin)
admin.site.register(DiaryComment)
