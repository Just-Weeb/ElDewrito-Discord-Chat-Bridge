import discord
import time
import threading
from websocket import create_connection
from discord_webhook import DiscordWebhook
import yaml
import sys

#quick check for YAML config file
if len(sys.argv) != 2:
    raise ValueError('Please provide config file')

#reading in config file to variable. Probably should do some input verification to prevent bad data being passed in
with open(sys.argv[1], "r") as ymlfile:
    cfg = yaml.load(ymlfile)

#assuming all config variables were entered in the yaml file
###########################  <Config>  ###################################
password = cfg["password"] #ed management password
server = cfg["server"] #ed server address
port = cfg["port"]
apiToken = cfg["apiToken"] #discord bot token
botName = cfg["botName"] #WEBHOOK NAME MUST MATCH BOT NAME
discordChan = cfg["discordChan"] #Channel you have configured the webhook on 
serverAdmin = cfg["serverAdmin"] #if anyone mentions a keyword notify the server admin in discord
webHook = cfg["webHook"] #webhook url
###########################  </Config>  ###################################

keywords = ['admin', 'hack', 'hacker', 'server', 'Admin']

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

#initiate our dewrito rcon connection
connectSock()


#thread to handle sending messages from dewrito to discord
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

        elif 'Join us on discord!' in result:
            continue

        else:
            for x in keywords:
                if x in result:
                    result = result + ' ' + serverAdmin
                    break

            webhook = DiscordWebhook(url=webHook, content=result)
            response = webhook.execute()


def motd():
    while True:

        try:
            ws.send("server.say Join us on discord! https://discord.gg/NxDpq2Z")

        except:
            continue

        time.sleep(1800)

#start our dewrito to discord bridge
x = threading.Thread(target=chatTX)
x.start()

#MOTD thread
y = threading.Thread(target=motd)
y.start()

client = discord.Client()

@client.event
async def on_ready():
    print('ohai {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
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
            ws.send('server.say {0.author.name}: {0.content}'.format(message))
        except Exception as e:
            print('Failed to connect, retrying...')
            connectSock()

client.run(apiToken)
