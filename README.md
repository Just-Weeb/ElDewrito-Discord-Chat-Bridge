# ElDewrito-Rcon-Python-Example
Example python client for the ElDewrito server.


## Sample commands:
```Server.Announce	1	Announces this server to the master servers
Server.AnnounceStats	1	Announces the players stats to the masters at the end of the game
Server.Connect 192.168.x.xxx	N/A	Begins establishing a connection to a server by providing the ip address
Server.Countdown	15	The number of seconds to wait at the start of the game
Server.KickBanIndex	kbi playername	kicks and IP bans the player from the game by index (host only)
Server.KickBanPlayer	kb playername	kicks and IP bans the player from the game by name (host only)
Server.KickBanUid	kbu playername	Kicks and IP bans the player from the game by Uid (host only)
Server.KickIndex	ki playername	kicks the player from the game by index (host only)
Server.KickPlayer	k playername	kicks the player from the game by name (host only)
Server.KickUid	ku playername	Kicks the player from the game by Uid (host only)
Server.ListPlayers	N/A	Lists players in the game (currently host only)
Server.Say - Sends a chat message as the server
Server.LobbyType	3	Changes the lobby type for the server. 0 = Campaign; 1 = Matchmaking; 2 = Multiplayer; 3 = Forge; 4 = Theater;
Server.MaxPlayers	16	Maximum number of connected players
Server.Mode	4	Changes the game mode for the server. 0 = Xbox Live (Open Party); 1 = Xbox Live (Friends Only); 2 = Xbox Live (Invite Only); 3 = Online; 4 = Offline;
Server.Name	HaloOnline Server	The name of the server
Server.Password	N/A	The server password
Server.Ping	N/A	Ping a server
Server.Port	N/A	The port number the HTTP server runs on, game uses different one
Server.ShouldAnnounce	1	Controls whether the server will be announced to the master servers
Server.SprintEnabled	1	Controls whether sprint is enabled on the server
Server.Unannounce	N/A	Notifies the master servers to remove this server
Server.UnlimitedSprint	0	Controls whether unlimited sprint is enabled on the server```
