# インストールした discord.py を読み込む
import asyncio
import discord
import re
from requests_html import AsyncHTMLSession , HTMLSession
#if asyncio.get_event_loop().is_running(): # Only patch if needed (i.e. running in Notebook, Spyder, etc)
import nest_asyncio
#nest_asyncio.apply()

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODMyMjk2NTgzMDg0NTA3MjA5.YHhumA.A1RMZ2NNOTpCGMFecRfSstfmw2Q'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 本体の実装
    if message.content == '/covid':
        amount = 0
        url = 'https://www3.nhk.or.jp/news/special/coronavirus/data/'
        nest_asyncio.apply()
        asession = AsyncHTMLSession()
        r = await asession.get(url)
        await r.html.arender()
        amount = re.findall('沖縄\n(.*)\n福岡', r.html.text)[0]
        await message.channel.send('今日の沖縄県のコロナの人数は'+amount+'人です。')


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
