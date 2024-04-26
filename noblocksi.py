import discord
from discord.ext import commands
import psutil
import os
import time


# Function to block applications
def block_applications(applications):
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] in applications:
                print(f"Detected {proc.info['name']} running. Terminating...")
                try:
                    os.system(f"TASKKILL /F /IM {proc.info['name']}")
                except Exception as e:
                    print(f"Error while terminating {proc.info['name']}: {e}")
        time.sleep(1)


intents = discord.Intents.all()
# Discord Bot setup
bot = commands.Bot(command_prefix='sudo ', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def block(ctx):
    await ctx.send('Blocking now')
    applications_to_block = ["java.exe", "javaw.exe"]  # Add the names of applications you want to block
    block_applications(applications_to_block)
    await ctx.send('Applications blocked successfully!')


# Run the bot
bot.run('MTIyOTcyNzIyOTM4MzI4Mjc0MQ.GPuo5j.eeiizozYP-0nDfmfj9BwQzWHBHabBp1tCI9MVQ')
