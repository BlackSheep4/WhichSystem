import subprocess
import re

print('[+] Welcome to WhichSystem')
target = input('[+] Please put the IP target: ')


ping = subprocess.Popen(f"ping {target}",shell=True,  stdout=subprocess.PIPE)
out = ping.communicate()[0] #access stdoutdata
out = out.split() #split by spaces
out = str(out)

ttl = re.search(r'TTL=(\d+)', out).group(1)
ttl= int(ttl)

if ttl >= 0 and ttl <= 64:
    print("Operative System --> Linux")
elif ttl >= 65 and ttl <= 128:
    print("Operative System --> Windows")
else:
    print("Unkown")