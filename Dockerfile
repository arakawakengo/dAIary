# ベースとなるイメージを指定
FROM python:3.11

# 環境変数を設定（Pythonが.pycファイルを作成しないようにする、Pythonが標準出力と標準エラー出力にバッファリングしないようにする）
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ワークディレクトリを設定
WORKDIR /

# 依存関係のコピー
COPY requirements.txt .

# 依存関係のインストール
RUN pip install -r requirements.txt

# プロジェクトのファイルをコピー
COPY . .

# ポート8000を開放
EXPOSE 8000

# アプリケーションの実行
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
