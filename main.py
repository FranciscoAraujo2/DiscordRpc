from pypresence import *
import time


ID = '' #https://discord.com/developers/applications


DETAILS = '🍓・Rpc made by KIKO#5148 '
STATE = "🫐・Houston, we've had a problem."
LOGO = 'logo'

#Buttons 
LABEL1 = '🐈 Github'
URL1 = 'https://github.com/FranciscoAraujo2'
LABEL2 = '📷 Instagram'
URL2 = 'https://www.instagram.com/francisco.araujo_2/'


#Dont touch

RPC = Presence(ID)
RPC.connect()

while True:
    RPC.update(
        details = DETAILS,
        large_image = LOGO, 
        buttons =[{"label": LABEL1, "url": URL1},{"label": LABEL2, "url": URL2}],
        state = STATE
    )
    print('Rpc made by KIKO#5148')
    time.sleep(600000)
