import discord
import threading
from websocket import create_connection
from discord_webhook import DiscordWebhook




###########################  Config  ###################################
password = '' #ed rcon password
server = '' #ed server address
port = '11776' #ed server rcon port
apiToken = '' #Discord bot token
botName = '' #name you gave the webhook. This is important as it prevents the chat from entering a spam loop
discordChan = '' #discord channel you want to bridge
serverAdmin = '' #if anyone mentions anything in keyword list notify the server admin in discord
webHook = '' #Webhook url for the bot you created
##########################  Config  ###################################



#build our dewrito rcon connection
def connectSock():
    try:
        global ws
        ws = create_connection("ws://" + server + ":" + port, subprotocols=["dew-rcon"])
        print("Connected!")
        ws.send(password)
        print("Authenticated!")
    except Exception as e:
        print("Failed to connect.")
        print(e)

#initiate our dewrito rcon connection
connectSock()


#thread to handle sending messages from dewrito to discord
def chatTX():
    while True:
        try:
            result =  ws.recv()
        except:
            connectSock()
            continue

        result = result.strip('<SERVER/0000000000000000/127.0.0.1>')

        if '<discord>' in result:
            continue

        else:
            webhook = DiscordWebhook(url=webHook, content=result)
            response = webhook.execute()


#start our dewrito to discord bridge
x = threading.Thread(target=chatTX)
x.start()


#start our discord to dewrito bridge
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
        elif message.author.name == botName: #Change zerogravity to the name of your discord bot
            #This is for future ability to chat both ways. Prevents infinite loop of bot chat.
            return
        elif message.channel.name != discordChan: #Name of the channel you want to forward to the ed server
            return
        else:
            #await message.channel.send('sent message!')
            try:
                ws.send('server.say <discord>{0.author}:{0.content}'.format(message))
            except Exception as e:
                print("Failed to connect, retrying connection...")
                connectSock()

client = MyClient()
client.run(apiToken)
