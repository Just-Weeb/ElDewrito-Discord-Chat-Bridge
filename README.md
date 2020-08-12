# ElDewrito Discord Chat Bridge and rcon interface.

```shell
sudo ./build.sh
```
DISCLAIMER: There is a lot of sensitive information stored in this script and it is intended as a proof of concept. Users will have to  accept all risks when running this.

You will need a discord bot api token and webhook url for the discord channel you plan on managing your ed server from. I recommend creating a specific channel for this with a custom discord role for access. You will also need your eldewrito server connection info and rcon credentials. If you would like discord mentions if players type keywords in chat you can enable this by providing your discord user id. See the sample config below for more info.

```
###########################  <Config>  ###################################
password = '' #ed management password
server = '' #ed server address
port = '11776'
apiToken = '' #discord bot token
botName = '' #WEBHOOK NAME MUST MATCH BOT NAME
discordChan = 'rcon' #Channel you have configured the webhook on 
serverAdmin = '' #if anyone mentions a keyword notify the server admin in discord. Format is <@useridhere> for users and <@&roleidhere> for roles.
webHook = '' #webhook url
motd_msg = '' #Any message you would like to be sent on a 30 minute loop to the ed chat
###########################  </Config>  ###################################
```

Once connected your discord channel will be linked with the Eldewrito server chat. Everything in this channel will be sent to the ed server chat and vise versa. You can also manage your eldewrito server with any of the following commands below by prefacing them with '!'. Bear in mind anyone with access to the discord channel will have access to these commands. Enjoy!

Example:

!server.listplayers

## Sample commands:
```
!playerstats
!serverstats
Server.AddBan - Adds to the ban list (does NOT kick anyone)
Server.Announce - Announces this server to the master servers
Server.AssassinationEnabled 0 - Controls whether assassinations are enabled on the server
Server.BottomlessClipEnabled 0 - Controls whether bottomless clip is enabled on the server
Server.CancelVote - Cancels the vote
Server.ChatCommandEndGameEnabled 1 - Controls whether or not players can vote to end the game.
Server.ChatCommandKickPlayerEnabled 1 - Controls whether or not players can vote to kick someone.
Server.ChatCommandShuffleTeamsEnabled 1 - Controls whether or not players can vote to shuffle the teams.
Server.ChatCommandVoteTime 45 - The number of seconds a chat command vote lasts
Server.ChatLogEnabled 1 - Controls whether chat logging is enabled
Server.ChatLogFile chat.log - Sets the name of the file to log chat to
Server.Connect - Begins establishing a connection to a server
Server.Countdown 5 - The number of seconds to wait at the start of the game
Server.CountdownLobby 3 - The number of seconds to wait in the lobby before the game starts
Server.Dedicated 1 - Used only to let clients know if the server is dedicated or not
Server.DualWieldEnabled 1 - Controls whether dual wielding is enabled on the server
Server.FloodFilterEnabled 1 - Controls whether chat flood filtering is enabled
Server.FloodMessageScoreLong 5 - Sets the flood filter score for long messages
Server.FloodMessageScoreShort 2 - Sets the flood filter score for short messages
Server.FloodTimeoutResetSeconds 1800 - Sets the period in seconds before a spammer's next timeout is reset
Server.FloodTimeoutScore 10 - Sets the flood filter score that triggers a timeout
Server.FloodTimeoutSeconds 120 - Sets the timeout period in seconds before a spammer can send messages again
Server.GamePort 11774 - The port number used by Halo Online
Server.HitMarkersEnabled 0 - Controls whether or not hitmarkers are enabled on this server
Server.Http.CacheTime 5 - Time in seconds the server should cache the http server response
Server.KickBanIndex - Kicks and IP bans a player from the game by index (host only)
Server.KickBanPlayer - Kicks and IP bans a player from the game by name (host only)
Server.KickBanUid - Kicks and IP bans players from the game by UID (host only)
Server.KickIndex - Kicks a player from the game by index (host only)
Server.KickPlayer - Kicks a player from the game by name (host only)
Server.KickTempBanPlayer - Kicks and temporarily IP bans a player from the game by name (host only)
Server.KickTempBanUid - Kicks and temporarily IP bans players from the game by UID (host only)
Server.KickUid - Kicks players from the game by UID (host only)
Server.ListPlayers - Lists players in the game
Server.LobbyType - Changes the lobby type for the server. 0 = Campaign; 1 = Matchmaking; 2 = Multiplayer; 3 = Forge; 4 = Theater;
Server.MapVotingTime 30 - Controls how long the vote lasts for Map Voting.
Server.MaxPlayers 16 - Maximum number of connected players
Server.Message - Text to display on the loading screen (limited to 512 chars)
Server.Mode - Changes the network mode for the server. 0 = Xbox Live (Open Party); 1 = Xbox Live (Friends Only); 2 = Xbox Live (Invite Only); 3 = Online; 4 = Offline;
server.name Halo Online Server - The name of the server (limited to 128 characters)
Server.NumberOfRevotesAllowed 3 - Controls how many revotes are allowed in the voting system
Server.NumberOfTeams 2 - Set the desired number of teams
Server.NumberOfVetoVotes 1 - Controls how many veto votes are allowed
Server.NumberOfVotingOptions 3 - Controls how many voting options are displayed
Server.PM - Sends a pm to a player as the server. First argument is the player name, second is the message in quotes
Server.Password - The server password
Server.Ping - Ping a server
Server.PlayersInfo {"0":{"r":0,"e":"http://new.halostats.click/emblem/emblem.php?s=100&0=0&1=0&2=5&3=2&fi=16&bi=51&fl=0&m=1"}} - Emblem and Rank info for each player
Server.Port 11777 - The port number the HTTP server runs on, the game uses Server.GamePort
Server.RconPassword ChangeMe - Password for the remote console
Server.ReloadVetoJson - Manually Reloads Json
Server.ReloadVotingJson - Manually Reloads Json
Server.Say - Sends a chat message as the server
Server.SendChatToRconClients 1 - Controls whether or not chat should be sent through rcon
Server.ShouldAnnounce 1 - Controls whether the server will be announced to the master servers
Server.ShuffleTeams - Evenly distributes players between the red and blue teams
Server.SignalServerPort 11779 - The port the signaling server will listen on
Server.SprintEnabled 0 - Controls whether sprint is enabled on the server
Server.SubmitVote - Sumbits a vote
Server.TeamShuffleEnabled 1 - Controls whether or not the teams will be automatically shuffled before the game starts.
Server.TeamSize 1 - Set the minimum number of players each team must have before a new team is assigned
Server.TempBanDuration 2 - Duration of a temporary ban (in games)
Server.TimeBetweenVoteEndAndGameStart 4 - Controls how many seconds to wait after a vote passes before calling 'game.start'.
Server.Unannounce - Notifies the master servers to remove this server
Server.Unban - Removes from the ban list
Server.UnlimitedSprint 0 - Controls whether unlimited sprint is enabled on the server
Server.VetoJsonPath mods/server/veto.json - Veto Json Path
Server.VetoSystemEnabled 0 - Controls whether the veto system is enabled on this server.
Server.VetoSystemSelectionType 0 - 0 for random, 1 for ordered
Server.VetoVotePassPercentage 50 - Percentage of players that need to vote for it to pass
Server.VetoVoteTime 20 - The time a veto vote takes
Server.VetoWinningOptionShownTime 10 - The length of time the winning option is show
Server.VotePassPercentage 50 - Percentage of players required to vote yes for a chat command vote to pass
Server.VotingDuplicationLevel 1 - Whether duplicate voting options will be allowed.
Server.VotingEnabled 1 - Controls whether the map voting system is enabled on this server.
Server.VotingJsonPath mods/server/voting.json - Voting Json Path
Server.WebsocketInfo - Display the websocket password for the current server
```
