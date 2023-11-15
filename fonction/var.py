import os, datetime, json
from colorama import *


class Const:
    ICO =Fore.RED + """
 ██▓     ▒█████   ▒█████   ██ ▄█▀  ██████ 
▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒ ▒██    ▒ 
▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ░ ▓██▄   
▒██░    ▒██   ██░▒██   ██░▓██ █▄   ▒   ██▒
░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒██████▒▒
░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░ ░▒  ░ ░
  ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ ░  ░  ░  
    ░  ░    ░ ░      ░ ░  ░  ░         ░ 
""" + Fore.LIGHTBLUE_EX
    X = Fore.LIGHTBLUE_EX +"https://twitter.com/exploitlover"
    DISCORD = Fore.LIGHTBLUE_EX + "https://discord.com/users/709428112739401860"
    TELEGRAM = Fore.LIGHTBLUE_EX + "https://t.me/ogfounder"

    HEADER = f"""
    {ICO}

    twitter(x) : {X}
    discord    : {DISCORD}    
    telegram   : {TELEGRAM}
"""+ Fore.WHITE
class AppInfo() : # Create App Class 

    def __init__(self, webhook : str or None) :
        try :
            self.os = os.name
            self.run_time = datetime.datetime.now()
            self.run_end = None
            if webhook is None :
                with open("config.json", "r") as f: 
                    file = json.load(f)
                if file["webhook"] == "" :
                    self.webhook = None
                else :
                    self.webhook = file["webhook"]
            else : 
                self.webhook = webhook
            self.logs = None
            self.output = "-lookup.txt"
            print(Fore.GREEN + "[APP ON]" + Fore.WHITE)
        except :
            print(Fore.RED + "[APP ERROR]" + Fore.WHITE)




              