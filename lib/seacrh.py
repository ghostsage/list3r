import requests
from colorama import Fore

try:
    class search:
        def __init__(self,target):
            self.target = target
            self.search()
        def search(self):                       
            with open('wordlist/large.txt','r') as file:
                for line in file:
                    char=line.strip()
                    url=self.target+'/'+ char
                    r=requests.get(url)
                    if r.status_code==200:
                        print(Fore.BLUE,'[+] Found:',url)               
                    file.close()
except requests.exceptions.ConnectionError:
    print(Fore.RED,'[!] Please check your url!')
except requests.exceptions.MissingSchema:
    print(Fore.RED,'[!] Please check your url!')
