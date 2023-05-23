from django.contrib import admin

# モデルをインポート
from . models import Diary, DiaryComment

# 管理ツールに登録
admin.site.register(Diary)
admin.site.register(DiaryComment)
