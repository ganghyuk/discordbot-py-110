from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("문의는 강혁#1647"))

@client.event

async def on_message(message):
    if message.content == "!ㅊㄱ": # 메세지 감지
        await message.channel.send (" {}, 님이 출근하셨습니다".format( message.author.mention))
    if message.content == "!ㅌㄱ": # 메세지 감지
        await message.channel.send (" {}, 님이 퇴근하셨습니다".format( message.author.mention))
    if message.content == "야이시잘년아": # 메세지 감지
        await message.channel.send (" 네? 주인님 부르셨어요? ")
    if message.content == "!강혁": # 메세지 감지
        await message.channel.send (" 저의 창조주이십니다. ♡ ")
    if message.content == "!슈_": # 메세지 감지
        await message.channel.send (" 귀여운거 보면 꼴리는 여자 ")
    if message.content == "!바다": # 메세지 감지
        await message.channel.send (" 서버 공식 귀요미입니다 ")
    if message.content == "!한": # 메세지 감지
        await message.channel.send (" 네 ")
    


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
    import discord, asyncio



    



