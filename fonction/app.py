import time
from fonction.var import *
from fonction.utils import *
from fonction.SocialsCheck import *

from colorama import *

async def app(username : str) :
    clear()
    app_instence = AppInfo()
    print(Const.HEADER)
    
    print(Fore.WHITE)
    print(f"username : {username}")
    print(Fore.GREEN + "lookup start in 10 seconde"+ Fore.WHITE)
    time.sleep(10)
    print("\n")
    SocialsInstence = Socials(username)
    SocialsResult = await SocialsInstence.main()
