# 同期無限Loop, 非同期Post
#  ▶ これではNG

import asyncio
from async_process import async_post, async_sleep

async def main():
    loop_count = 0
    url = 'http://localhost:8080/'

    # 💬イベントループの取得
    loop = asyncio.get_event_loop()
    try:
        while True:
            loop_count += 1
            # 非同期かつバックグラウンド実行
            asyncio.ensure_future(async_post(url, loop_count))
            # 非同期に1秒間スリープ(このコードをベースにキックする。)
            # loop.run_until_complete(async_sleep(0.1))
            await asyncio.sleep(0.1)

    except KeyboardInterrupt:  # CTRL+C で終了
        pass
    finally:
        loop.close()

# if __name__ == "__main__":
#     main()


# イベントループを取得
loop = asyncio.get_event_loop()

# イベントループで main コルーチンを実行
loop.create_task(main())

# イベントループを永続的に実行
loop.run_forever()


'''
# 気になることをつぶす

-----------------------------------
## 1.非同期の書き方
-----------------------------------
@asyncio.coroutine = python3.4から。
async, await = python3.5から。          ◀ 💬こっちを使う。✅await方式に書き直す。

-----------------------------------
## 2.非同期処理で必要となる処理
-----------------------------------
① … イベントループの取得
    loop = asyncio.get_event_loop()
② … session。使ったほうが実装しやすい。
    session = aiohttp.ClientSession()
③ … asyncio.ensure_future(async_post(session, loop_count))を読み解く
    … async_post() ▶ コルーチン関数
    … asyncio.ensure_future(...)
         … └> 引数のコルーチンobjをasyncタスクとしてスケジューリング
         … └> 引数のコルーチンを受け取り、それをFutureオブジェクトにラップ
             … Futureオブジェクト
                └> 注文待ち札のイメージ。まだ利用できない結果。予約のほうが近いか？
                └> コールバックを持つ。操作が完了したら特定のアクションを自動実行できる
                └> 💬async def で定義された関数 … ではない。これはCoroutin関数
             … Coroutin関数
                └> async def で定義された関数。
                └> 呼び出すとコルーチンオブジェクトが返される。
                └> コルーチンオブジェクトを実行すると、その結果や進行情報を保持する`Future`オブジェクト（具体的にはTaskオブジェクト）が関与する。


④ … async def async_post() は、非同期関数を呼び出せる関数コルーチン関数。関数自体が非同期関数は❌
    … コルーチン内部では、コードは上から下へと順番に実行される。
⑤ … yield from（async）の役割は？
     … 非同期処理の中で、他の非同期処理を待機する際に、仕様される。
         … 💬5loopに一回止まっているのはこれで納得。終わった瞬間に吐き出されるのも納得。
             … 💬処理が全てFIFOってわけではない。
⑥ … スケジューリングされて、実行されてないasyncタスクの数って見れる？ ▶ yes
     … scheduled_callbacks = len(loop._ready)
         … 非同期関数内でsleepを設定することで、現在実行されてないasyncタスク数を増やせた
            … sleep中は他の非同期タスクやコルーチンがイベントループで実行される

⑦ … run_until_complete, 指定されたコルーチンが完了するまで、この関数はブロックする。勿論引数にはコルーチンを設定。

'''