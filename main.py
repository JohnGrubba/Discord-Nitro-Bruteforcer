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

██████╗░██████╗░██╗░░░██╗████████╗███████╗███████╗░█████╗░██████╗░░█████╗░███████╗██████╗░
██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░█████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░██████╔╝
██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░██╔══██╗
██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝
""")
print("Made by Jonas Grubbauer")
num=input('How Many Codes to Generate and Check: ')

f=open("GeneratedCodes.txt","w", encoding='utf-8')

print("Generating Codes!")
time.sleep(2)
#Codes Generator

for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")
   print('Generating Codes:', n+1)

f.close()

#Bruteforcer
x = 0
print("All Codes have been generated!\n")
print("Hit Enter to start Checking your codes!")
input()
print("Checking",n+1,"Codes now!")
time.sleep(3)
with open("GeneratedCodes.txt") as f:
    for line in f:
        nitro = line.strip("\n")
        x = x + 1
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" YOU GOT ONE! | {} ".format(line.strip("\n")))
            break
        elif r.status_code == 429:
            print("Too many requests! Rate Limit!")
        else:
        	print(" Invalid | {} | ".format(line.strip("\n")), x)
print("Checked all Codes! No one was working! I'm sorry... ")
print("Now hit Enter to Kill the Program!")
input()