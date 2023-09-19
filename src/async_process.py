import aiohttp
# import asyncio


class ClientSessionManager:
    # 💬sessionは外に出す。
    def __init__(self):
        self.session = aiohttp.ClientSession()

    # 非同期Post
    async def async_post(self, url, loop_count):

        data = {'loop_count': str(loop_count)}
        # 💬post前チェック
        print("🟠Sending request for loop_count: {}".format(loop_count))
        response = await self.session.post(url, data=data)
        text = await response.text()
        # 💬post後チェック
        print("🟨Received response for loop_count {}".format(text))

        return text

    async def close(self):
        if self.session:
            await self.session.close()
