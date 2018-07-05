import asyncio
from aiohttp.client import ClientSession


async def download_to_file(client: ClientSession, url: str, save_to: str):
    async with client.get(url) as response:
        if response.status != 200:
            raise ValueError(f'Status {response.status} for {url}')

        with open(save_to, mode='wb') as f:
            f.write(await response.read())


async def download_multiple(url_start: str, url_endings: list):
    async with ClientSession() as client:
        await asyncio.gather(*(download_to_file(client, url_start + x, x) for x in url_endings))


def __main__():
    url_start = 'https://get4.sweetbook.net/b/5154/_T6aFZeZ6OOz73RFeY1vn5Z_ip7kKk-yi1HG9KEw90A,/'
    #endings = ['01_%02d_Ustrashenie.mp3' % x for x in range(1, 16)]
    endings = ['02_%02d_Kleschi.mp3' % x for x in range(1, 15)]
    asyncio.get_event_loop().run_until_complete(download_multiple(url_start, endings))


if __name__ == '__main__':
     __main__()
