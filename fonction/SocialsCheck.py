import aiohttp, json, asyncio
from colorama import *
from bs4 import BeautifulSoup



class Socials():
    def __init__(self, username: str):
        self.username = username
        self.urllist = ["https://twitter.com/", "https://tiktok.com/@", "https://instagram.com/", "https://github.com/", "https://facebook.com/", "https://www.snapchat.com/add/", "https://www.youtube.com/@"]
        self.results = {}

    async def main(self):
        self.requestlist = [self.request(url) for url in self.urllist]
        responses= await asyncio.gather(*self.requestlist)

        for url, response, content  in zip(self.urllist, responses[0], str(responses[1])):
            self.results[url] = response
            soup = BeautifulSoup(content , 'html.parser')
            print(content + '\n\n')
            try :
                title = soup.title.string
                facebook = soup.find_all(class_ ='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xtoi2st x3x7a5m x1603h9y x1u7k74 x1xlr1w8 xi81zsa x2b8uid')      
            except :
                title = None
                facebook = None
            
            if response == 200 :
                if url in ["https://twitter.com/", "https://instagram.com/","https://facebook.com/" ,  "https://www.youtube.com/@"] :
                    if url == "https://www.youtube.com" and title == '404 Not Found': 
                        self.results[url] = 404 
                        print(Fore.RED  + f"[-] {url}{self.username}")
                    elif url == "https://www.instagram.com" and title == 'Page introuvable • Instagram' :
                        self.results[url] = 404 
                        print(Fore.RED  + f"[-] {url}{self.username}")    
                    elif url == "facebook.com" and facebook == 'Ce contenu n’est pas disponible pour le moment':
                        self.results[url] = 404 
                        print(Fore.RED  + f"[-] {url}{self.username}")      
                    elif url == "https://twitter.com" and title.find(self.ursernames)  :
                        self.results[url] = 404 
                        print(Fore.RED  + f"[-] {url}{self.username}") 
                    else :                             
                        print(Fore.GREEN + f"[+] {url}{self.username}")
            else :
                print(Fore.RED  + f"[-] {url}{self.username}")
        print(self.results)
        return self.results

    async def request(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{url}{self.username}") as response:
                return response.status, await response.text()

        
        