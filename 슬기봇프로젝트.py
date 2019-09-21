import discord
import os

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
    if message.content.startswith("!스릇"):
        await message.channel.send("스릇@ㅅ@ https://mimgnews.pstatic.net/image/382/2018/10/11/0000680201_001_20181011170800004.jpg?type=w540")
    if message.content.startswith("!제작자"):
        await message.channel.send("즐겜유저#2815")
    if message.content.startswith("!양동욱"):
        await message.channel.send("어...라... http://imgnews.naver.net/image/382/2017/11/11/0000606159_002_20171111100555401.jpg")   
    if message.content.startswith("!아이린"):
        await message.channel.send(" 헉 여신님 http://cafefiles.naver.net/MjAxOTA4MTlfNyAg/MDAxNTY2MjE3OTI1ODc1.u27tZHRBvubCYXnXqoYtRvPOL9FI97VdsxzMzhCALhgg.tI3hgDgLhNg60AM1hWf1vwWyks_gQRlvoWvkIU-mbuwg.GIF/externalFile.gif")  
    if message.content.startswith("!웬디"):
        await message.channel.send("날개없는 천사님 !! http://kinimage.naver.net/20170720_244/1500483055312wWhUl_JPEG/1500483055171.jpg")
    if message.content.startswith("!레드벨벳"):
        await message.channel.send("심쿵 흐잇 http://post.phinf.naver.net/MjAxOTAyMTNfNjcg/MDAxNTUwMDI5NjIyMzc3.u4pgJ3xM1J2tBHOhARaUr7ouaQMFbOgTdz4XcNF5Opwg.v-Pty9P0JkUWWM4DFpNchzbBqpZwx4WJuFCf7yM7MtYg.JPEG/IG7hgcFe1-oKZ1bMUe6ZyDtsuyt8.jpg")
    if message.content.startswith("총"):
        await message.channel.send("빵야 http://blogfiles.naver.net/MjAxODEyMjNfMjg1/MDAxNTQ1NTQ0ODI5NDk0.SDTE0rsI-DuMXdoOej0Y6pWPAbaJeM2F7sVTHsBbgPAg.AepiPkEUAXR2pJ28VuYMud4IeMJK2qNgjBrqbtPZJFIg.JPEG.exia9133/1545544829532.jpg")
    if message.content.startswith("!섹시"):
        await message.channel.send("허으윽 ㅜㅜ http://imgnews.naver.net/image/433/2018/11/21/0000052156_001_20181121135904641.jpg")
    if message.content.startswith("!짐살라빔"):
        await message.channel.send("마법의주문 짐살라빔 짐살라빔~ http://blogfiles.naver.net/MjAxOTA2MTlfNiAg/MDAxNTYwOTQ3MTU1NDQ2.mm2sPHRf2hAhswQ4XLUt2LvFv-LzK4y_kyJ0_pKrj3sg.anGkqyHhCdC6IKCxY0AZIBrRGCjtaE5qcC2dGCVTWBgg.GIF.kmh33080/9985323C5D0A087B1E1C6E.gif")
    if message.content.startswith("!RBB"):
        await message.channel.send("으 무셔 http://blogfiles.naver.net/MjAxODExMzBfMiAg/MDAxNTQzNTgyMDMwMDM0.6xdxqob27d9XCDjns1c4WD2NrVx0_AbR_-zMRbQnH7sg.N9-9oK_eoz9ZGQ9oAVq3L7JEbhJukkC657WKI7_l_wcg.GIF.mxnxmood/9907D8455C01114220.gif")
    if message.content.startswith("!BadBoy"):
        await message.channel.send("현혹된다아...http://blogfiles.naver.net/MjAxODAyMDJfMjYw/MDAxNTE3NTU2MTAxOTAy.l8sIp3tnyUt2PbiTKUMqvxm8vNQ8LDbLb0VLtSK2N7Ag.5vg1SrRtWd32PNVPWw_cxeLtaz-PDJ7e0_SWKji3wDwg.GIF.xxxsss123/%B7%B9%BA%A709.gif")
    if message.content.startswith("!음파음파"):
        await message.channel.send("음파 음파 헤헤 http://blogfiles.naver.net/MjAxOTA4MjBfMjE4/MDAxNTY2MjYwODg3Mjg3.-3d4__BoXWVvcTEPUWS8zqzI1FWxdBuUlofljo8MVM0g.gJQbZ_nMdRx8Err5Ut2sT2-79UMEnj7Cf07TqGwnhqcg.GIF.snanyilovem/IMG_7685.GIF")
    if message.content.startswith("!피카부"):
        await message.channel.send("피카부우~~ 뭔가 무섭당 http://blogfiles.naver.net/MjAxNzExMTdfODkg/MDAxNTEwOTI3OTM1NjE0.-YplUURU_lB_UL_raZthz_9S0qjYtASRVe8oF-kgQcgg.TNgDEKupOx9xLlUrkKzdPU2-3WdEnGhyUJ8qMsZFZegg.GIF.uni_l/1510921583150.GIF")
    if message.content.startswith("!파워업!Power up"):
        await message.channel.send("빠빠나나나나 빠빠나나나나 http://cafefiles.naver.net/MjAxODEwMDJfOCAg/MDAxNTM4NDkxMDIxMDg4.JP7ZMfUT0Xjq2DCTOsayyeWjfdUiZfcS3D-ZdxhBxeMg.DjL2PieNYWWWi0uKTNbxOhGQGIHYp_2R2xP1cmAw5dUg.GIF.jjae0613/externalFile.GIF ")
    if message.content.startswith("!러시안룰렛"):
        await message.channel.send("커지는 Heart B-B-Beat~~http://blogfiles.naver.net/20161003_140/pinkensullove_1475461645517OLJyT_GIF/2016_10_1_52.gif")
    if message.content.startswith("!행복 happiness")
        await message.channel.send("모든것의 시작 !http://blogfiles.naver.net/20140801_122/nwowolf_1406893454497NBxdV_GIF/C41C51.GIF")
    if message.content.startswith("!빨간맛"):
        await message.channel.send("빠바빨간맛 궁금해허니~! http://blogfiles.naver.net/MjAxNzA3MTZfMTY1/MDAxNTAwMTkyNDc3OTUw.IB_x7YoJmgbwgA8LBHf-ujk8H4BWo3tT6XBaAEynQFog.w3JUcEKM2bP2cpM2CqsX2yyQ4P4-d2HL8p1hWVbYeBIg.GIF.ghkdlxmtlem/tumblr_ost36liEXs1tizu4so4_540.png")
    if message.content.startswith("!7월7일"):
        await message.channel.send("우리 다시만나.... http://blogfiles.naver.net/20160322_262/a1b2d3f4g5_14586362332421g5g7_GIF/pikicast-249873820.gif")
    if message.content.startswith("!3가지소원"):
        await message.channel.send("제소원은... ㅎ http://kinimage.naver.net/20151230_64/1451484555864EhSIl_JPEG/1451484555584.jpg")
    if message.content.startswith("!여름빛"):
        await message.channel.send("너는나의 모히또~~♥ http://blogfiles.naver.net/MjAxNzA3MTFfMjg5/MDAxNDk5NzYzMDgxODA4.PjitdVe4f3FJKZa4wUbKMEWfyCdk_FOBRxiyil7b62Eg.ocJdDBrZI1d5NMOY_bIMTRT4I-MglNdJ5EfjnEF5yMUg.GIF.onlyjeeone/%C1%A6%B8%F1-%BE%F8%C0%BD-8.gif")
     if message.content.startswith("!Be Natural"):
        await message.channel.send("내심장..허억.... ♥♥ http://blogfiles.naver.net/MjAxODEyMjlfODEg/MDAxNTQ2MDY3MTM2OTE5.pZ9Wr0ztxt7FeJvlGSgWX2pmgeW6jEc5YF_EvAj6uZEg._UIbF9S6zA51cvxQiNTlzjSe13kAEz3OtSnI83jMwtMg.GIF.kmh33080/99DE95415C263C4012.gif")
     if message.content.startswith("!조이"):
        await message.channel.send("비율쩐당 http://kinimage.naver.net/20160221_99/1456037668157zxMKw_JPEG/IMG_20151111_160759.jpg")
     if message.content.startswith("!예리"):
        await message.channel.send("마성의 매력이랄까? http://imgnews.naver.net/image/433/2018/12/21/0000053330_001_20181221122002648.jpg")
    if message.content.startswith("!명령어"):
        await message.channel.send("!안녕,!슬기,!사랑해,!박수,!제작자,!아이린,!웬디,!레드벨벳,!총,!섹시,!짐살라빔,!RBB,!BadBoy,!음파음파,!피카부,!러시안룰렛,!행복 happiness,!빨간맛,!7월7일,!3가지소원,!여름빛,!Be Natural,!예리,!조이")
        
        
        
        
        
        
        
        
access_token - os.environ["Bot_Token"]        
client.run(access_token)
