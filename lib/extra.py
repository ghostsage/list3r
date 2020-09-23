import random
from colorama import Fore
from pyfiglet import Figlet

class extra:
    def print_cool_text(self,color,text):
        style=Figlet(font='slant')
        print(color,style.renderText(text))
    def usage(self):
        print(Fore.RED,'[!] Usage; python3 main.py <targeturl>')    
    def pick_random(self,list):
        return random.choice(list)    