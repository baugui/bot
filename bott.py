import discord
from discord.ext import commands
from IA import get_class
Import OSErrorImport requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def hello(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            nombre = attachment.filename
            direccion = attachment.url
            await attachment.save(f'./{attachment.filename}')
    else:
        await ctx.send("No funciona")
        await ctx.send(get_class(image_path=f'./{attachment.filename}',model_path=f'./keras.model.h5' ), labels_path='./labels.txt')
    
        

bot.run("MTIxNzUyMTgyNzE4NzAwMzQyMw.GJ8w9v.j8z8R5bk3kEthgPfC52YSNQX6cqiIDOBkEeNzQ")