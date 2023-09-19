import aiohttp
import asyncio

async def async_post(url, loop_count):

    # await asyncio.sleep(0.1)

    session = aiohttp.ClientSession()

    data = {'loop_count': str(loop_count)}
    # 💬post前チェック
    print("🟠Sending request for loop_count: {}".format(loop_count))
    response = await session.post(url, data=data)
    text = await response.text()
    # 💬post後チェック
    print("🟨Received response for loop_count {}".format(text))

    # session を閉じる
    await session.close()


    return text

async def async_sleep(seconds):
     await asyncio.sleep(seconds)
