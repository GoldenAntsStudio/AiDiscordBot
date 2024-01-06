import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

TOKEN = 'MTE5MzE0OTU5Mzk1Nzk3NDAzOA.GXvDML.6eNv1_MMq63Xla6nPFDATX1sFhaH8JtkhSI1ck'

# команды
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(image=f'./{attachment.filename}', model="C:/Users/tikho/Desktop/3dGame/keras_model.h5", labels='labels.txt'))
    else:
        await ctx.send('Вы забыли прикрепить картннку :()')

bot.run(TOKEN)
