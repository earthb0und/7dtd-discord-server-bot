# 7dtd-server-bot

a discord bot that has the ability to control a 7DTD linux GSM based server

# How to use it
1. clone or downlond the script from the main branch
2. place main.py in your root sdtd directory (usually ./sdtdserver on default GSM configs)
3. create a token.ini alongside the main script, or just run the main script and it will create one for you
4. In the token.ini, create or add the line:
   token='YOUR TOKEN HERE'
Provide your token WITHOUT the quotes ''.
5. Run the main script using python or python3 main.py, the script will first look for a bot token and immediately connect to discord
6. You can use commands like '-start server' which will directly run the command for starting the server. The bot has some mitigation against command expolotation but like most things like this you should be very cautious with who you give this type of priviledge to. Perfect for private servers I wouldn't use this on a community discord without privileges.

# Commands
- bot status
-start server
-stop server
-restart server
-details
