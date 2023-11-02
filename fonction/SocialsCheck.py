import aiohttp, json, asyncio
from colorama import *




class Socials():
    def __init__(self, username: str):
        self.username = username
        self.urllist = ["https://twitter.com/", "https://tiktok.com/@", "https://instagram.com/", "https://github.com/", "https://facebook.com/", "https://linkedin.com/in/", "https://www.snapchat.com/add/", "https://www.youtube.com/@"]
        self.results = {}

    async def main(self):
        self.requestlist = [self.request(url) for url in self.urllist]
        responses = await asyncio.gather(*self.requestlist)

        for url, response in zip(self.urllist, responses):
            self.results[url] = response

            if response == 200 or  response == 999:
                print(Fore.GREEN + f"[+] {url}{self.username}")
            else :
                print(Fore.RED  + f"[-] {url}{self.username}")
        return self.results

    async def request(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{url}{self.username}") as response:
                return response.status

        
        