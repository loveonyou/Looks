import os, argparse, asyncio, sys
from fonction.app import *
from colorama import *


__author__ = "adn"
__version__ = "0.4-beta"

if __name__ == "__main__":
    init()
    parser = argparse.ArgumentParser( # setup args parser
        prog= 'LookTools', # setup program name
        description= 'Osint tools for look up peusdo and get all information available on the network.',
        add_help= True 

    )
    parser.add_argument('-u', dest= "username", help='user peusdo you want to found', required=True) # add args username 
    #parser.add_argument('-e', dest= "email", help='email you want to found', required=False) in dev 
    #parser.add_argument('-n', dest= "number", help='number peusdo you want to found', required=False) in dev 
    parser.add_argument('-w', dest= "webhook", help='webhook discord for output and logs', required=False) # add args webhook
    parser.add_argument('-v', dest = "version", action='version', version=f'%(prog)s {__version__}')
    args = parser.parse_args() 
    username = args.username 
    webhook = args.webhook
    #email = args.email
    #number = args.number 
    try : 
        os.system(f"title LookTools user {os.getlogin()}") # setup title of terminal windows
    except OSError : 
        print("\033]0;LookTools user {}\a".format(os.getlogin())) # setup title of terminal linux
    
    asyncio.run(app(username, webhook))
