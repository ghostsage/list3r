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
    if len(sys.argv)<1:
        extra().usage()
        sys.exit()

    target=sys.argv[1]
    print(target)
    wordlist_type=input("Enter the type of wordlist [s/m/l]: ")
    if wordlist_type.lower()=='s':
        wordlist='small'
    elif wordlist_type.lower()=='m':
        wordlist='medium'    
    elif wordlist_type.lower()=='l':
        wordlist='large'    
    else:
        print(Fore.RED,'[!] Please type a valid argument!')    
        exit()
    search().search(target,wordlist)
except KeyboardInterrupt:
    print(Fore.RED,'[*] Quiting ...')    
except EOFError:
    print(Fore.RED,'[*] Quiting ...')    