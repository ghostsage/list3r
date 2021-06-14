from colorama import Fore
import subprocess
from lib.extra import extra
import sys
from lib.seacrh import search

colors=[Fore.RED,Fore.BLUE,Fore.YELLOW,Fore.GREEN]
color=extra().pick_random(colors)

try:
    subprocess.call('clear',shell=True)
    extra().print_cool_text(color,'List3r')
    if len(sys.argv)<2:
        extra().usage()
        sys.exit()

    target=sys.argv[1]
    print('[+] Target: ',target)
    wordlist='large'
    search().search(target,wordlist)
except KeyboardInterrupt:
    print(Fore.RED,'[*] Quiting ...')    
except EOFError:
    print(Fore.RED,'[*] Quiting ...')    
