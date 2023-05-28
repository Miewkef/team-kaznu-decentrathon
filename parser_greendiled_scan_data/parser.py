import asyncio

import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import asyncio

BASE_URL = "https://greenfieldscan.com/"
HEADERS = {"User-Agent": UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")
            body = soup.find('div', {'class': 'css-1uool25'})
            items = body.find("tbody") \
                                        .find_all('tr')
            for i in items:
                name = i.p.text
                links = i.find_all('a')[1:]
                hashes = []
                for j in links:
                    item = j['href'].split('/')
                    hashes.append(item[2])

            

if __name__ == '__main__':
    asyncio.run(main())