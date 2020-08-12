import discord
import time
import threading
import urllib.request
import json
from websocket import create_connection
from discord_webhook import DiscordWebhook


###########################  Config  ###################################
password = '' #ed management password
server = '' #ed server address
port = '11776' #server port
apiToken = '' #discord bot api token
botName = '' #Webhook name MUST match bot name
discordChan = 'rcon' #Discord channel name you want to manage from
serverAdmin = '<@&roleIDnumber>' #if anyone mentions hack or admin keyword notify the server admin role in discord
webHook = 'https://discordapp.com/api/webhooks/'
motd_msg = 'Join us on discord! discord.gg'
dew_api = 'http://yourserverip:11775'
##########################  Config  ###################################

keywords = ['admin', 'hack', 'hacker', 'server', 'Admin']

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
            break

        result = result.strip('<SERVER/0000000000000000/127.0.0.1>')

        if '<discord>' in result:
            continue

        elif motd_msg in result:
            continue

        else:
            for x in keywords:
                if x in result:
                    result = result + ' ' + serverAdmin
                    break

            try:
                webhook = DiscordWebhook(url=webHook, content=result)
                response = webhook.execute()

            except:
                print("Discord webhook rate limit reached! (probably)")

def server_meta():
    try:
        with urllib.request.urlopen(dew_api) as url:
            data = json.loads(url.read().decode())

        payload = "Players: {}, Status: {},  Map: {}, GameType: {}".format(data["numPlayers"], data["status"], data["map"], data["variant"])

        try:
            webhook = DiscordWebhook(url=webHook, content=payload)
            response = webhook.execute()

        except:
            print("Failed to connect to the discord webhook url.")

    except:
        print("Could not connect to the dewrito meta data api.")


def player_meta():
    players = ["```"]

    try:
        with urllib.request.urlopen(dew_api) as url:
            data = json.loads(url.read().decode())

        for player in data["players"]:
            players.append("{} - Alive: {}, Kills: {}, Deaths: {}, Betrayals: {}, Suicides: {}".format(player["name"], player["isAlive"], player["kills"], player["deaths"], player["betrayals"], player["suicides"]))

        players.append("```")

        players = "\n".join(players)

        try:
            webhook = DiscordWebhook(url=webHook, content=str(players))
            response = webhook.execute()

        except:
            print("Failed to connect to the discord webhook url.")

    except:
        print("Could not connect to the dewrito meta data api.")


def motd():
    while True:
        time.sleep(1800)
        try:
            ws.send("server.say " + motd_msg)

        except:
            continue

            
x = threading.Thread(target=chatTX)
x.start()

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
        if message.content[1:] == "serverstats":
            server_meta()

        elif message.content[1:] == "playerstats":
            player_meta()

        else:
            ws.send(message.content[1:])
            print(message.content[1:])

    else:
        try:
            ws.send('server.say {0.author}:{0.content}'.format(message))

        except:
            print('Failed to connect, retrying...')
            connectSock()

client.run(apiToken)
