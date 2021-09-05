import discord
import re
import json
from requests_html import AsyncHTMLSession
from discord.ext import tasks
from datetime import datetime

TOKEN = ''
client = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    if datetime.now().strftime('%H:%M') == '20:30':
        msg = await get_today_covid_num_on_okimawa()
        print(msg)
        ch_id = 771304861139861504
        channel = client.get_channel(ch_id)
        await channel.send(msg)

@client.event
async def on_message(message):
    msg=''
    if message.author.bot:
        return
    if message.content == '/covid':
        msg = await get_today_covid_num_on_okimawa()
        await message.channel.send(msg)

async def get_today_covid_num_on_okimawa():
    num=0
    url = "https://www3.nhk.or.jp/n-data/special/coronavirus/data/latest-pref-data.json"
    asession = AsyncHTMLSession()
    r = await asession.get(url)
    dic = r.json()
    pref=dic["data47"]
    num=0
    for i in pref:
        if i["name"]=="沖縄県":
            num=i["new"]
    today = dic["lastmodifed"]
    print(num)
    return today+'現在の沖縄県のコロナの人数は'+str(num)+'人です。'

with open("token.txt",'r') as fr:
    TOKEN = fr.read()

loop.start()
client.run(TOKEN)