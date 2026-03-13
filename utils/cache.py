import aiohttp

cache = {}

async def get_image(url):
    if url in cache:
        return cache[url]

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.read()

    cache[url] = data
    return data