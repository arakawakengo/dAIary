# kyodai_flea_market_app
Practice of Infomation System 8班

## Task List
1. HomePages
2. Back-end service
3. DataBase

## 環境構築 / Build a development environment
- リポジトリをclone / Clone this repository
```
git clone https://github.com/arakawakengo/kyodai_flea_market_app.git
```

* [Setting Git](Guidance/Git.md)
* [Setting Django](Guidance/django.md)
* [Setting Vue](Guidance/Vue.md)

## Introduce the public Path
### This is project path that all the top level
```shell
workspace/kyodai_flea_market_app
```
### This is Back-end service path that all of the service will storage in this path, like receive request from homepage.
```shell
workspace/kyodai_flea_market_app/PoIS
```

### This is Vue path that all of the html file and function will storage in this path. Almost all of our work in the first phase is carried out here.
### Please familiarize yourself with all the files under this folder first. 
```shell
workspace/kyodai_flea_market_app/templates
```



## VueとDjangoのサーバーを起動できるか確認 / Check if you can start Vue or Django server
### Vue
- ```/kyodai_flea_market_app/```フォルダにいることを確認 / Make sure you are in ```/kyodai_flea_market_app/```
```shell
cd templates
npm run serve
```
http://localhost:8080/ にアクセスしてVueの画面が表示されればOK

Go to http://localhost:8080/ and if you see the Vue screen, you're good to go.


### Django
- ```/kyodai_flea_market_app/```フォルダにいることを確認 / Make sure you are in ```/
kyodai_flea_market_app```

```python
python manage.py runserver
```

http://localhost:8000/ にアクセスしてDjangoの画面が表示されればOK

Go to http://localhost:8000/ and if you see the Django screen, you're good to go.

## Gitの使い方 / How to use Git
### 基本的な作業フロー
- 自分の作業ブランチを作って、そのブランチで作業をします。
- 作業内容を自分のPC(ローカル)からGithub上(リモート)にpushします。
- github上で、プルリクエスト(自分の作業ブランチの内容をmainブランチに取り込むようにお願いをする手順)を作ります。
- 他の人が変更内容を確認して、問題がなさそうならマージ(変更内容をmainなどの他のブランチに取り込むこと)します。
- 以上のフローによって、mainブランチには必ず動作する完全なコードを置いておくことができます！

### ブランチを作る / Create a branch
```
git branch [branch_name]
```
### ブランチを移動 / Switch to a branch
```
git checkout [branch name]
```
### 自分のブランチした作業を確定してリモートにpushする
作業の前に、```git branch```で自分の作業ブランチにいるかどうかを確認することが大事です
```
git add .
git commit -m "commit message"
git push origin [branch_name]
```
commit messageには、自分のした変更内容が良く分かるようなコメントをつけます。

[branch_name]は自分の作業ブランチの名前が入ります。

### リモートのブランチの更新をローカルのブランチに取り込む / Incorporate updates from remote branches into local branches
他の人のPR(プルリクエスト)がマージされたとき、自分のPCにあるローカルのmainブランチにはその変更は反映されていません。
その変更を自分のPCに取り込むために以下の作業をします。
- ローカルのmainブランチをリモートのmainブランチの状態に更新する
```
git checkout main
git pull origin main
```
### 最新にしたローカルのmainブランチの内容を自分の作業ブランチに反映する
ローカルのmainブランチを更新した後は、自分の作業ブランチにもその変更を反映させる必要があります。
まず、自分のブランチに移動した後、git mergeコマンドを実行します。
```git merge origin main```で、mainブランチの内容を今いるブランチ[your_branch_name]に反映します。
```
git checkout [your_branch_name]
git merge origin main
```
