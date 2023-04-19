# kyodai_flea_market_app
Practice of Infomation System 8班

# Recommond system

## This is the introduce doc to inite the git

## step 1

Install Git.

```shell

# enter the codebase path
cd workspace/
# check the dir
ls -a
# inite the code base
git init
# setup your username 
git config --global user.name "username"
# setup your email address
git config --global user.email "...@gmail.com"

# checking your setting info

git config --global --list

# setting remote code base url 
git remote add origin git@github.com:arakawakengo/kyodai_flea_market_app.git

# setting ssh key
ssh-keygen -t rsa -C "username"
```
![rsa key](img/20200810174740183.png)
```
# enter the dir that storage ssh key 
cd ~/.ssh
# show the file 
ls
# show the content of rsa key
cat id_rsa.pub
```
![id_rsa.pub](img/20200810180651227.png)
### Paste the id_rsa.pub to Github
![key gitbub](img/20200810181625337.png)

### Test the Link 
![add key to github](img/20200810181903438.png)

```
ssh -T git@github.com
```
### push your code to remote branch

```
git push -u origin main
```

## 環境構築 / Build a development environment
- リポジトリをclone / Clone this repository
```
git clone https://github.com/arakawakengo/kyodai_flea_market_app.git
```
- Djangoのインストール / Install Django
```
cd kyodai_flea_market_app
pip install django
```

- Vue.jsのインストール / Install Vue.js
```
cd market_app
npm install
```
### 備考 / Note
- ```npm install```は、```/kyodai_flea_market_app/market_app/```で実行すること。
- ```npm install``` を実行することで、market_app/package.jsonに定義されているパッケージ(Vueなど)をまとめてインストールできます。
- ```npm install`` should be run in ```/kyodai_flea_market_app/market_app/``.
- By running ```npm install```, the packages (Vue, etc.) defined in market_app/package.json can be installed at once.


## VueとDjangoのサーバーを起動できるか確認 / Check if you can start Vue or Django server
### Vue
- ```/kyodai_flea_market_app/```フォルダにいることを確認 / Make sure you are in ```/kyodai_flea_market_app/```
```
cd market_app
npm run serve
```
http://localhost:8080/ にアクセスしてVueの画面が表示されればOK

Go to http://localhost:8080/ and if you see the Vue screen, you're good to go.


### Django
- ```/kyodai_flea_market_app/```フォルダにいることを確認 / Make sure you are in ```/
kyodai_flea_market_app```

```
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