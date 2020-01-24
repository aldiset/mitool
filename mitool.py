from os import *
import socket
from colorama import Fore

class Main():
    '''{><}'''

    def __init__(self, run):
        self.run

    def run(self):
        system("clear")
        print("::--------------------------------------------------::")
        print("::++++++++++++++++++++++++++++++++++++++++++++++++++::")
        system("figlet -f /usr/share/figlet/figlet-fonts/3d.flf mitool | lolcat")
        print("::++++++++++++++++++++++++++++++++++++++++++++++++++::")
        print("::--------------------------------------------------::")
        print("[+]+++++++++ mitool v1.0  beta")
        print("[+]+++++++++ Author : Aldi ")
        print("[+]+++++++++ Suhu born of noob people \n\n")
        print(Fore.RED+"[+] Options\n")
        print(Fore.BLUE+"[1] SQL Injection")
        print("[2] Payload ")
        print("[3] DDos \n")

        self.options=input(Fore.GREEN+"[-] What your options ? ")
        



Main("aku").run()
