import serial
import time
import requests
import json

URL = "http://34.68.143.162/bruh.php?url="


ser = serial.Serial("com4", 9600)
print("connected")
#ser.open()
time.sleep(2)

while(True):
    bruh = input("enter gyazo img link: ")
    r = requests.get(URL + bruh).json()
    try:
        if r["status"] == True:
            ser.write(b'1\n')
            print("incorrect spelling!")
        else:
            print("correct spelling!")

    except:
        print("correct spelling")
