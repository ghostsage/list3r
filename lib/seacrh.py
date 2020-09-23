import requests
from colorama import Fore

class search:
    def search(self,target,wordlist_type):
        if wordlist_type=='small':
            with open('wordlist/small.txt','r') as file:
                for line in file:
                    char=line.strip()
                    url=target+'/'+ char
                    r=requests.get(url)
                    if r.status_code==200 or r.status_code==403:
                        print(Fore.BLUE,'[+] Found:',url)
            file.close()
        elif wordlist_type=='medium':
            with open('wordlist/medium.txt','r') as file:
                for line in file:
                    char=line.strip()
                    url=target+'/'+ char
                    r=requests.get(url)
                    if r.status_code==200 or r.status_code==403:
                        print(Fore.BLUE,'[+] Found:',url)   
            file.close()                       
        elif wordlist_type=='large':
            with open('wordlist/large.txt','r') as file:
                for line in file:
                    char=line.strip()
                    url=target+'/'+ char
                    r=requests.get(url)
                    if r.status_code==200 or r.status_code==403:
                       print(Fore.BLUE,'[+] Found:',url)               
            file.close()            