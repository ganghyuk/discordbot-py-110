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
    if message.content == "!환영 (message,mention)": # 메세지 감지
        await message.channel.send (" 네모바지 스폰지밥🧽  서버에 오신걸 환영해요 ෆ
                                    새로운 뉴페 {}  님 등장하셨습니다 
                                    다들 환영 해주세요 (´∇｀)
                                    （📄）：규칙사항  서버 규칙 꼭 읽어주시고 
                                    （☄）：역할소개   역할 모르는게 있다면 이거 확인 해주세요
                                    그리고 적응이 안되신다면 @“ 🌱 ” ：적응이 필요해요!   태그 해주세요.
                                    또한 궁금한 점있으시면 ⁠（📮）：건의사항 에서 궁금한거 질문해주시면 감사하겠습니다.
                                    @“ 💧 ” ：새로운 주민이 왔어요! ".format( message.author.mention))


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
    import discord, asyncio



    



