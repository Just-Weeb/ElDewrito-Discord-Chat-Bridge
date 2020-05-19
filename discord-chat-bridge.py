import discord
import threading
from websocket import create_connection
from discord_webhook import DiscordWebhook


###########################  Config  ###################################
password = '' #Eldewrito server rcon password
server = '' #Eldewrito server address
port = '11776' #Eldewrito server rcon port
apiToken = '' #Your discord bot API token
botName = '' #The name you gave your webhook bot. This is import or else the chat bridge will enter a spam loop
discordChan = '' #Channel you want to bridge to your Eldewrito server
serverAdmin = '<@12345678910111213>' #your user id if you want notifications enabled (You will have to turn on discord developer mode to get this. Role ID's work as well.)
webHook = '' #Discord server webhook url
keywords = ['admin', 'hack', 'hacker', 'server', 'Admin'] #Keywords you would like to be notified on
##########################  Config  ###################################


#Build our dewrito rcon connection
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

#Initiate our dewrito rcon connection
connectSock()


#Thread to handle sending messages from dewrito to discord
def chatTX():
    while True:
        try:
            result =  ws.recv()
        except:
            connectSock()
            break

        result = result.strip('<SERVER/0000000000000000/127.0.0.1>')

        if '<discord>' in result:
            continue

        else:
            for x in keywords:
                if x in result:
                    result = result + ' ' + serverAdmin
                    break

            webhook = DiscordWebhook(url=webHook, content=result)
            response = webhook.execute()


#Start our dewrito to discord bridge
x = threading.Thread(target=chatTX)
x.start()


#Start our discord to dewrito bridge
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        elif message.author.name == botName:
            return
        elif message.channel.name != discordChan:
            return
        elif '!' in message.content[0]:
            ws.send(message.content[1:])
            print(message.content[1:])
        else:
            try:
                ws.send('server.say <discord>{0.author}:{0.content}'.format(message))
            except Exception as e:
                print("Failed to connect, retrying connection...")
                connectSock()

client = MyClient()
client.run(apiToken)
