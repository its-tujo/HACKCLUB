import os
import time
import sys
import requests
import asyncio



#Some definitions

async def print_joke():
    requests.get("https://official-joke-api.appspot.com/jokes/random/1").json()
    joke = requests.get("https://official-joke-api.appspot.com/jokes/random").jsonclea





print(" Hello World!")
print("yipppppp.py is running...")
print("Current working directory:", os.getcwd())
print("List of files in current directory:", os.listdir('.'))
print("Python version:", sys.version)
print(" ")
print("Current time:", time.ctime())

print("A Joke for you:")
time.sleep(1)
asyncio.run(print_joke())
time.sleep(1)
if 1 == 1:
    print("Continuing the program...")
    time.sleep(1)
    name= input("What is your name? ")
    time.sleep(1)
    if time.localtime().tm_hour < 12:
        print("Good morning " + name + "!")
    elif time.localtime().tm_hour < 18:
        print("Good afternoon " + name + "!")   
    elif time.localtime().tm_hour < 24:
        print("Good evening " + name + "!")
    elif time.localtime().tm_hour < 0:
        print("Good night " + name + "!")
    elif time.localtime().tm_hour < 6:
        print("Good night " + name + "!")
                    
else:

    print("Exiting the program...")
    time.sleep(2)
    print("Stop exiting, you can't stop NOW!!!!!!")
    time.sleep(2)
    print("Just kidding, Goodbye!")
    sys.exit()  
