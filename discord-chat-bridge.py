import discord
from websocket import create_connection


#Currently this only works going from discord to your ed server. 
password = "" #ed management password
server = "" #ed server address
port = "11776"

try:
    ws = create_connection("ws://" + server + ":" + port, subprotocols=["dew-rcon"])
    print("Connected!")
    ws.send(password)
    print("Authenticated!")
except Exception as e:
    print("Failed to connect.")
    print(e)
    exit()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            #await message.channel.send('bot name detected')
            return
        elif message.author.name == 'zerogravity': #Change zerogravity to the name of your discord bot
            #This is for future ability to chat both ways. Prevents infinite loop of bot chat.
            return
        elif message.channel.name != 'dewrito-chat': #Name of the channel you want to forward to the ed server
            return
        else:
            #await message.channel.send('sent message!')
            ws.send('server.say <discord>{0.author}:{0.content}'.format(message))

client = MyClient()
client.run('') #discord api token goes here
