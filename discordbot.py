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
    await client.change_presence(status=discord.Status.online, activity=discord.Game(" 강혁최강 "))

@client.event

async def on_message(message):
    if message.content == "!ㅊㄱ": # 메세지 감지
        await message.channel.send (" {}, 님이 출근하셨습니다".format( message.author.mention))
    if message.content == "!ㅌㄱ": # 메세지 감지
        await message.channel.send (" {}, 님이 퇴근하셨습니다".format( message.author.mention))
    if message.content == "!예은": # 메세지 감지
        await message.channel.send (" 큐티뽀짝 서버대표 기요미 ")
    if message.content == "!강혁": # 메세지 감지
        await message.channel.send (" 저의 창조주이시고, 이 서버의 최강존잘지존이십니다 . ♡ ")
    if message.content == "!슈_": # 메세지 감지
        await message.channel.send (" 귀여운거 보면 꼴리는 여자 ")
    if message.content == "!바다": # 메세지 감지
        await message.channel.send (" 서버 공식 귀요미입니다 ")
    if message.content == "!한": # 메세지 감지
        await message.channel.send (" 네 ")
    if message.content == "!일영": # 메세지 감지
        await message.channel.send (" 이서버 대표 또라이 입니다 ")
    if message.content == "!다원": # 메세지 감지
        await message.channel.send (" 서버 공식 집착녀입니다 ")
    if message.content == "!레트": # 메세지 감지
        await message.channel.send (" 이거 보면 나랑 친구해쥬! ")
    if message.content == "!돼지": # 메세지 감지
        await message.channel.send (" 서버 최강 가수 기요미 돼지 ")
    if message.content == "!ㅁㅑ": # 메세지 감지
        await message.channel.send (" 서버에서 유일한 정상적인 사람입니다 ")
    if message.content == "!삼점": # 메세지 감지
        await message.channel.send (" 친구가 필요합니다. ")
    if message.content == "!고뤠": # 메세지 감지
        await message.channel.send (" 발로란트 같이 해주세요 ")
    if message.content == "!아루루": # 메세지 감지
        await message.channel.send (" 카트 중섭 아랭 500위 한섭 스랭 마스터 고인물 입니다.  ")
    
    

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
    import discord, asyncio



    



