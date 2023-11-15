import aiohttp, json, asyncio
from colorama import *
from bs4 import BeautifulSoup
from pydantic import BaseModel


class ReponseModel(BaseModel): # build model of request reponse
    
    url : str
    username : str
    code : int 
    title : str or None


class Socials():
    def __init__(self, username: str):
        self.username = username
        self.urllist = ["https://tiktok.com/@", "https://instagram.com/", "https://github.com/", "https://facebook.com/", "https://www.snapchat.com/add/"]
        self.results = {}

    async def main(self):
        self.requestlist = [self.request(url) for url in self.urllist] # create a list of requests
        responses = await asyncio.gather(*self.requestlist) 

        for url, response in zip(self.urllist, responses):
            self.results[url] = response[0]
            soup = BeautifulSoup(response[1] , 'html.parser')
            try : 
                title = soup.title.string
            except :
                title = None

            response_dict = ReponseModel( # formatted reponse
                title= title,
                url= url,
                code= response[0],
                username= self.username
            )
            if response_dict.code == 200 :  # re check the reponse status and format then  
                if  response_dict.url in ["https://instagram.com/","https://facebook.com/"] :
                    if response_dict.url == "https://instagram.com/" and response_dict.title == "Instagram":
                        self.results[response_dict.url] = 404
                    elif response_dict.url == "https://facebook.com/" and response_dict.title == "Facebook":
                        self.results[response_dict.url] = 404
                    else :
                        self.results[response_dict.url] = 200
                elif response_dict.url in  ["https://tiktok.com/@", "https://github.com/", "https://www.snapchat.com/add/"] : 
                    self.results[response_dict.url] = 200
                
        results = self.results
        for result_url , code in results.items() : # print result
            if code == 200 :
                print(Fore.GREEN + f"[+] {result_url}{self.username} " + Fore.WHITE)
            elif code == 404 :
                print(Fore.RED + f"[-] {result_url}{self.username} " + Fore.WHITE)
            else : 
                print(Fore.YELLOW + f"[ERROR] {result_url}{self.username} ")

        
            
    async def request(self, url):
        async with aiohttp.ClientSession() as session: # insitials the session and do the request
            async with session.get(f"{url}{self.username}") as response: 
                return response.status, await response.text()