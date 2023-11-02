import os, datetime
from colorama import *


class Const:
    ICO = """
 ██▓     ▒█████   ▒█████   ██ ▄█▀  ██████ 
▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒ ▒██    ▒ 
▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ░ ▓██▄   
▒██░    ▒██   ██░▒██   ██░▓██ █▄   ▒   ██▒
░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒██████▒▒
░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░ ░▒  ░ ░
  ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ ░  ░  ░  
    ░  ░    ░ ░      ░ ░  ░  ░         ░ 
"""
    X = "https://twitter.com/exploitlover"
    DISCORD = "https://discord.com/users/709428112739401860"
    TELEGRAM = "https://t.me/ogfounder"

    HEADER = f"""
    {ICO}

    twitter(x) : {X}
    discord    : {DISCORD}    
    telegram   : {TELEGRAM}
"""
class AppInfo() :

    def __init__(self):
        try :
            self.os = os.name
            self.run_time = datetime.datetime.now()
            self.run_end = None
            self.webhook = None
            self.logs = None
            print(Fore.GREEN + "[APP ON]" + Fore.WHITE)
        except :
            print(Fore.RED + "[APP ERROR]" + Fore.WHITE)




              