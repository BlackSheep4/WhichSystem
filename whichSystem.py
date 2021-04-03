import subprocess
import re
import os
import time
import platform

print("""
_       ____  ______________  __   _______  _____________________  ___
| |     / / / / /  _/ ____/ / / /  / ___/\ \/ / ___/_  __/ ____/  |/  /
| | /| / / /_/ // // /   / /_/ /   \__ \  \  /\__ \ / / / __/ / /|_/ / 
| |/ |/ / __  // // /___/ __  /   ___/ /  / /___/ // / / /___/ /  / /  
|__/|__/_/ /_/___/\____/_/ /_/   /____/  /_//____//_/ /_____/_/  /_/   
                                                                       """)

time.sleep(1)
print('\n')
print('[+] Welcome to WhichSystem')
target = input('[+] Please put the IP target: ')

system = platform.system()

if system == 'Windows':
    try:
        ping = subprocess.Popen(f"ping {target}",shell=True,  stdout=subprocess.PIPE)
        out = ping.communicate()[0] #access stdoutdata
        out = out.split() #split by spaces
        out = str(out)

        ttl = re.search(r'TTL=(\d+)', out).group(1)
        ttl= int(ttl)

        if ttl >= 0 and ttl <= 64:
            print("[!] Operative System --> Linux")
        elif ttl >= 65 and ttl <= 128:
            print("[!] Operative System --> Windows")
        else:
            print("Unkown")
    except (AttributeError):
        print('\n')
        print('[!] An error occurred. It is possible that the server is down or that you have misspelled the IP or domain.')

elif system == 'Linux':
    ping = subprocess.Popen(f"ping -c 1 {target}",shell=True,  stdout=subprocess.PIPE)
    out = ping.communicate()[0] #access stdoutdata
    out = out.split() #split by spaces
    out = str(out)

    ttl = re.search(r'ttl=(\d+)', out).group(1)
    ttl= int(ttl)

    if ttl >= 0 and ttl <= 64:
        print("[!] Operative System --> Linux")
    elif ttl >= 65 and ttl <= 128:
        print("[!] Operative System --> Windows")
    else:
        print("Unkown")

else:
    print('Bro Apple is for rich people. Are u fucking rich?')
