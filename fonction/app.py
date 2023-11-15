import time
from fonction.var import *
from fonction.utils import *
from fonction.SocialsCheck import *

from colorama import *

async def app(username : str, webhook : str or None) :
    clear()
    app_instence = AppInfo(webhook) # create an instance for app
    print(Const.HEADER) # print header of tools
    print(Fore.WHITE)

    print(f"username : {username}")
    print(Fore.GREEN + "lookup start in 10 seconde"+ Fore.WHITE)
    time.sleep(10)
    print("\n")

    SocialsInstence = Socials(username) # run the social check
    SocialsResult = await SocialsInstence.main() # recover the result of check
