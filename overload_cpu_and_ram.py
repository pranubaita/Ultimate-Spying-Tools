import discord
from discord.ext import commands
import psutil
import time
import multiprocessing


def increase_cpu_usage(end_time):
    while True:

        for _ in range(10 ** 7):
            pass

        if time.time() > end_time:
            break



def increase_ram_usage(end_time):
    data = bytearray(1024 * 1024 * 1024 * 5)
    while True:
        if time.time() > end_time:
            break


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='sudo ', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def start(ctx, arg):
    await ctx.send('Starting slow down process.')
    if arg.isdigit():

        end_time = time.time() + int(arg)

        num_cores = psutil.cpu_count()

        processes = []
        for _ in range(num_cores):
            cpu_process = multiprocessing.Process(target=increase_cpu_usage, args=(end_time,))
            ram_process = multiprocessing.Process(target=increase_ram_usage, args=(end_time,))
            processes.append(cpu_process)
            processes.append(ram_process)
            cpu_process.start()
            ram_process.start()

        for p in processes:
            p.join()

        await ctx.send('Processes started successfully!')
    else:
        await ctx.send('Invalid argument. Please use "sudo start [value]" to start the processes.')


# Run the bot
bot.run('NUH-UH')
