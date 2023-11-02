import os, datetime
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
class AppInfo() :

    def __init__(self):
        try :
            self.os = os.name
            self.run_time = datetime.datetime.now()
            self.run_end = None
            self.webhook = None
            self.logs = None
            self.output = "-lookup.txt"
            print(Fore.GREEN + "[APP ON]" + Fore.WHITE)
        except :
            print(Fore.RED + "[APP ERROR]" + Fore.WHITE)




              