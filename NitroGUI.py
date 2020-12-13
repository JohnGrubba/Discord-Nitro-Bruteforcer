import tkinter as tk
from tkinter import *
import os
import random, string
import webbrowser
import time
import requests

root = tk.Tk()
root.title('Discord Nitro Checker') 
root.geometry('400x300') 
root.resizable(0, 0)

T = Text(root, height=1, width=30)
T.pack()
T.insert(END, "DISCORD NITRO CHECKER GUI")
T.config(state=DISABLED)

T1 = Text(root, height=1, width=30)
T1.pack()
T1.insert(END, "How many Codes to Check:")
T1.config(state=DISABLED)


e = Entry(root)
e.pack()


def StartChecker():
      clear = lambda: os.system("cls")
      clear()
      print("Made by Jonas Grubbauer")
      print("-------------------------")
      num=e.get()

      #Bruteforcer
      x = 0

      for n in range(int(num)):
        pass
        nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 429:
          T2 = Text(root, height=1, width=50)
          T2.pack()
          T2.insert(END, "You have been Rate Limited! Wait some Time!")
          T2.config(state=DISABLED)
          break
        elif r.status_code == 200:
          print(" VALID |",nitro)
          T4 = Text(root, height=1, width=50)
          T4.pack()
          T4.insert(END, "VALID, CHECK THE CONSOLE!",nitro)
          T4.config(state=DISABLED)
          break
        else:
          print("INVALID",nitro, x,)
          T3 = Text(root, height=1, width=50)
          T3.pack()
          T3.insert(END, "Not working: ",x)
          T3.config(state=DISABLED)
        x = x + 1
        
      print("-------------------------")
      print("Checked",x,"Codes!")






runChecker = tk.Button(root, text="Run Checker!", padx=10,
                       pady=5, fg="white", bg="#263D42", command=StartChecker)
runChecker.pack()

root.mainloop()
