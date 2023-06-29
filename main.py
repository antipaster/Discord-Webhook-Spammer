import requests
import os
from pystyle import Colors, Center, Colorate

os.system('color')
while True:
    msg = input("Please Insert webhook Spam Message: ")
    webhook = input("Please Insert webhook URL: ")
    def spam(msg, webhook):
        for i in range(35):
            try:   
                data = requests.post(webhook, json={'content': msg})
                if data.status_code == 204:           
                     print(Colors.green + '[+] Sent')
            except:
                print( Colors.red+'[-] Invalid Webhook')
                exit()

    counts = 0.5
    while counts == 0.5:
        spam(msg, webhook)