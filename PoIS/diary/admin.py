from django.contrib import admin

# モデルをインポート
from . models import Diary

# 管理ツールに登録
admin.site.register(Diary)
