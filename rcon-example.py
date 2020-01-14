from websocket import create_connection

password = "" #ed server password
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

while True:
    n = input("\nTerminal: ")
    print(n)
    if n == "exit":
        ws.close()
        exit()
    ws.send(n)
    result =  ws.recv()
    print("Received '%s'" % result)
