import random, string
import webbrowser
import time
import requests
import os

clear = lambda: os.system("cls")
clear()
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
num=input('How many Codes to Check through! (You can enter numbers like 2 Billion! It wont crash!) ')

#Bruteforcer
x = 0

for n in range(int(num)):
  pass
  nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
  
  url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

  r = requests.get(url)

  if r.status_code == 429:
    print("""-------------------------
    You are being rate limited! You may wait some time!
    -------------------------""")
    input("Hit Enter to Exit!")
    break
  elif r.status_code == 200:
    print(" VALID |",nitro)
    break
  else:
    print("INVALID",nitro, x,)
  x = x + 1
  
print("-------------------------")
print("Checked",x,"Codes!")       