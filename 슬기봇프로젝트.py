import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("슬기 덕질하는중~")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요ㅎㅅㅎ")
    if message.content.startswith("!슬기"):
        await message.channel.send("슬기는 사랑입니당 ㅎ http://imgnews.naver.net/image/5359/2019/08/18/0000328800_001_20190818164003565.jpg")
    if message.content.startswith("!사랑해"):
        await message.channel.send("사랑합니다ㅎ http://blogfiles.naver.net/MjAxODEyMTVfMjUy/MDAxNTQ0ODY0MDUzNDU0.YL8qgFFVsU3WpzmMN2VJ8GrfM6TFibOg2p7i3t5qXMkg.8ZwVAuZzJp0P7wNmiPx7M6B-THPWhud5pPxquaoq_LUg.JPEG.velvetpoint13/redvelvetreveluv-20181215-174132-003.jpg")
    if message.content.startswith("!박수"):
        await message.channel.send("짝짝짝!! https://tenor.com/view/seulgi-kang-seulgi-%ec%8a%ac%ea%b8%b0-red-velvet-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-gif-14354373")
    if message.content.startswith("!즐겜"):
        await message.channel.send("네?http://imgnews.naver.net/image/433/2018/11/21/0000052157_001_20181121135917797.jpg")


client.run("NTUxNjIwNjkwOTE1MzYwNzc0.XW99QA.UXXa1dp9uF2DOELL0w31rn-sbUM")
