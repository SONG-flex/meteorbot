import discord
import time
import os


client = discord.Client()
channel = '659332802638118933', '677853265043521546'
@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("MADE by ! 백구#3155"))

    while True:
        await client.get_channel(int(channel)).send("@everyone```안녕하세요. 메테오 서버 홍보 담당입니다.```       ```혹시 새롭고 깔끔한 서버를 원하시나요? 아니면 재밌고 편하게 즐길 서버를 원하시나요? 그러면 즉시 저희 서버 와서 구경해보세요. 남들과는 다른 엄청난 노력으로 관리를 하기에 유저분들은 깔끔하고 재밌는 서버에서 몸만 들고 오셔도 됩니다. 그냥 즐기세요~~ 자 이제부터 그러면 저희서버의 장점 몇가지만 말하도록 하겠습니다.```       ```1. 다양한 로그 관리로 핵이 없고 비매너 유저가 없는 서버```      ```2. 지금까지 한번도 논란이 없는 관리자들 항시 대기.```     ```3. 💰 뉴비지원금 15억```     ```4.다양한 이벤트[레이싱&UFC&랜덤박스 한정차량 포함]```     ```5.현재 킬베로스, 범서방파 조직원 모집중. 얼른 와서 신청하세용.^3^```    ```6.다양한 특수직업 및 일반직업```    ```7.후원자들을 위한 특별한 후원제도 및 다양한 스킨.[추가하고싶으신거 있으시면 건의해주시면 됩니다.]```    ```8. 건의 시 개발자 바로 패치 준비.```        ```새로 리뉴얼 되서 더 나은 서버로 유저들에게 다가가겠습니다.지금까지 길었던 홍보내용을 봐줘서 진심으로 감사의 말씀드립니다. 많이 와주세요.```      https://discord.gg/qUCKTZV")
        time.sleep(7200) #초단위로 쿨타임을 센다.


token=os.environ["TOKEN"]
client.run
