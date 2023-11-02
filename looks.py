import os, argparse, asyncio
from fonction.app import *
from colorama import *

__author__ = "adn"
__version__ = "0.1"

if __name__ == "__main__":
    init()
    parser = argparse.ArgumentParser(
        prog= 'LookTools',
        description= 'Osint tools for look up peusdo and get all information available on the network.',
        add_help= True

    )
    parser.add_argument('-u', dest= "username", help='user peusdo you want to found', required=True)
    parser.add_argument('-v',  action='version', version=f'%(prog)s {__version__}')
    args = parser.parse_args()
    username = args.username

    os.system(f"title LookTools user {os.getlogin()}")  

    
    asyncio.run(app(username))
