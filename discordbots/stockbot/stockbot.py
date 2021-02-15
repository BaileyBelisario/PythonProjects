import discord
from discord.ext import commands
from time import sleep
import bs4
import requests
from bs4 import BeautifulSoup as bs

BOT_TOKEN = 'BOT TOKEN HERE'

class MyClient(discord.Client):

    # On ready, the bot will identify a channel ID you specify to send a message to
    # This channel should be private and called stockbot
    # Note you will need to allow the bot to manage nickname and change nickname on integration, then allow it to see the private channel

    async def on_ready(self):
        channel = client.get_channel(810266123764629595)
        await channel.send('AAPL - GD')


    # On a message from the bot itself, it will identify the stock symbol given and use some web scraping from yahoo.finance to find the info
    # You should only need change the stock symbol within the channel.send above and message.content below
    # Code isn't like fully perfect cause yahoo could change the classes or whatever in the futrue for the scraping, but it's an easy fix
    # The bot will run continuously in the while loop so it is recommended to background the script
    async def on_message(self, message):
        if message.content == 'AAPL - GD':
            if message.author.id == client.user.id:
                stock = message.content.split(" ")[0]
                link = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock
                
                while True:
                    url = requests.get(link)
                    soup = bs(url.text, features="lxml")
                    price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
                    try:
                        percentage = soup.find_all("span", {'class' : 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'})[0].text
                    except:
                        percentage = soup.find_all("span", {'class' : 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'})[0].text
                    nickname = stock + ' - ' + price
                    await message.author.edit(nick=nickname)
                    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=percentage))
                    sleep(.5)

client = MyClient()
client.run(BOT_TOKEN)
