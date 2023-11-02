import os

def clear():
    os_name = os.name
    if os_name == "nt":  
        os.system("cls")
    else:  
        os.system("clear")