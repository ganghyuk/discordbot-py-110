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
    if message.content == "!출근": # 메세지 감지
        await message.channel.send (" {}, 님이 출근하셨습니다".format( message.author.mention))
    if message.content == "!퇴근": # 메세지 감지
        await message.channel.send (" {}, 님이 퇴근하셨습니다".format( message.author.mention))
    if message.content == "!환영": # 메세지 감지
        await message.channel.send (" {}, @1092851225193615440  서버에 오신걸 환영해요 ෆ

새로운 뉴페 {}  님 등장하셨습니다 
다들 환영 해주세요 (*´∇｀*)

#1092781944078602300  서버 규칙 꼭 읽어주시고 

#1092752067866673213   역할 모르는게 있다면 이거 확인 해주세요

그리고 적응이 안되신다면 @1092847130382700664  태그 해주세요.
또한 궁금한 점있으시면 #1092782372623224913 에서 궁금한거 질문해주시면 감사하겠습니다".format( message.author.mention))


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
    import discord, asyncio



    



