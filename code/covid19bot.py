import discord
import re
from requests_html import AsyncHTMLSession , HTMLSession

TOKEN = 'ODMyMjk2NTgzMDg0NTA3MjA5.YHhumA.A1RMZ2NNOTpCGMFecRfSstfmw2Q'
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/covid':
        amount = 0
        url = 'https://www3.nhk.or.jp/news/special/coronavirus/data/'
        asession = AsyncHTMLSession()
        r = await asession.get(url)
        await r.html.arender()
        amount = re.findall('沖縄\n(.*)\n福岡', r.html.text)[0]
        await message.channel.send('今日の沖縄県のコロナの人数は'+amount+'人です。')

client.run(TOKEN)
