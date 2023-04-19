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

* [Setting Git](Guidence/Git.md)
* [Setting Django](Guidence/django.md)
* [Setting Vue](Guidence/Vue.md)

## 关于公文文件目录的说明
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
workspae/kyodai_flea_market_app/market_app
```



## VueとDjangoのサーバーを起動できるか確認 / Check if you can start Vue or Django server
### Vue
- ```/kyodai_flea_market_app/```フォルダにいることを確認 / Make sure you are in ```/kyodai_flea_market_app/```
```shell
cd market_app
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
