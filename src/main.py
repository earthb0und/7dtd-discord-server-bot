import discord
from discord.ext import commands
import subprocess
import sys

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)
command_prefix = "-"

try:
    with open("token.ini", 'r') as f:
        token = f.readline()
        print(token[6:])
        TOKEN = None if token[6:] == "'YOUR TOKEN HERE'" else token[6:]
except Exception as e:
    with open("token.ini", "w") as f:
        f.write("token='YOUR TOKEN HERE'")
        TOKEN = None

def run_command(command: str):
    if command == "start server":
        command  = ['./sdtdserver', 'start']
    elif command == "stop server":
        command = ['./sdtdserver', 'stop']
    elif command == "details":
        command == ['./sdtdserver', 'details']
    elif command == "restart server":
        command == ['./sdtdserver', 'restart']
    # Run the command and capture the output
    try:
        result = subprocess.run(command, capture_output=True, text=True)
    except Exception as e:
        return (f"SERVER RESP: {e}")
    
    # Check if the command was successful
    if result.returncode == 0:
        print("SERVER RESP:")
        print(result.stdout)
        if '[  OK  ] Starting sdtdserver: 7DTD - The Council Server' in result.stdout:
            return "The server was sucessfully started!"
        elif '[  OK  ] Stopping sdtdserver: 7DTD - The Council Server' in result.stdout:
            return "The server was sucessfully stopped."
        return result.stdout
    else:
        print("Error running command:")
        print(result.stderr)
        return "Error running command!"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message: str):
    # Prevent the bot from responding to itself
    if message.author == bot.user:
        return

    # Check if the message mentions the bot and says testing
    if message.content.lower() == command_prefix + 'bot status':
        await message.channel.send('Bot is healthy and active')

    elif message.content.lower() == command_prefix + 'start server':
        await message.channel.send('Starting the 7DTD Server')
        result = run_command("start server")
        await message.channel.send(result)

    elif message.content.lower() == command_prefix + 'stop server':
        await message.channel.send('Gracefully shutting down server...')
        result = run_command('stop server')
        await message.channel.send(result)
    
    elif message.content.lower() == command_prefix + 'restart server':
        await message.channel.send('Asking the server to restart...')
        result = run_command('restart server')
        await message.channel.send(result)

    elif message.content.lower() == command_prefix + 'details':
        await message.channel.send('Checking server status...')
        result = run_command('details')
        await message.channel.send(result)
    else:
        await message.channel.send('Invalid command!')

if TOKEN != None:
    bot.run(TOKEN)
else:
    print("Bot token not set or incorrect.")
    sys.exit(1)
