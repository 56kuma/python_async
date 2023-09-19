# python_async

## memo
Pythonのasync/awaitの挙動確認用

## 確認したいこと
Pythonのasync/awaitの挙動確認用
構成は以下の通り。

* Webサーバ … 同期
* Client … 非同期

## 起動
```sh
# コンテナ作成&起動
docker-compose build
docker-compose up -d

# コンテナ内部に入る
docker exec -it python_async

# コンテナ内部でサーバ側を起動
python3 ./src/A_receive_post_sync_return_loop-count.py
# コンテナ内部でクライアント側を起動
python3 ./src/C_aiohttp_post_infinity_paraller_send_sync.py
```
