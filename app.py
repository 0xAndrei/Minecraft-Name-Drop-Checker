from requests import get
from discord_webhook import DiscordWebhook
from time import sleep

URL = "https://api.mojang.com/users/profiles/minecraft/"
WEBHOOKURL = ""

Names = open('names.txt', 'r').read().splitlines() 

def check():
    for name in Names:
        req = get(URL+name)
        print(req.status_code)
        if req.status_code == 200:
            print(f"{name} is not dropping")
        if req.status_code == 204:
            print(f"{name} is dropping")
            webhook = DiscordWebhook(url=WEBHOOKURL, rate_limit_retry=True, content=f'**{name}** is dropping or blocked\nhttps://namemc.com/{name}') 
            webhook.execute()
        
        sleep(0.5)


while True:
    
    check()
    