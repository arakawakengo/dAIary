# ベースとなるイメージを指定
FROM node:lts-alpine

# ワークディレクトリを設定
WORKDIR /

# 依存関係のコピー
COPY package*.json ./

# 依存関係のインストール
RUN npm install

# プロジェクトのファイルをコピー
COPY . .

# ポート8080を開放
EXPOSE 8080

# アプリケーションのビルド
CMD ["npm", "run", "serve"]
