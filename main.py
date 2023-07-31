import disnake
from disnake.ext import commands
from typing import Optional

bot = commands.Bot(command_prefix='!', intents=disnake.Intents.all())

BLACKLIST = ['cука', 'дебил', 'блять']
TOKEN = 'YOUR TOKEN'


@bot.event
async def on_ready():
    print(f'Бот {bot.user} включен')


@bot.event
async def on_message(ctx: disnake.Message):
    if ctx.author.bot:
        return

    for i in BLACKLIST:
        if i in ctx.content.lower():
            await ctx.delete()
            await ctx.author.send('Так делать нельзя')
    return ctx


@bot.command()
async def ping(ctx: commands.Context):
    await ctx.channel.send('pong')
    await ctx.message.delete()


@bot.command(name='av')
@commands.is_owner()
async def avatar(ctx: commands.Context, user: Optional[disnake.User]=None):
    await ctx.message.delete()

    if user is None:
        await ctx.channel.send(ctx.author.avatar)
        return

    if not isinstance(user, disnake.User):
        await ctx.channel.send('Обнаружено неизвестное существо')
        return


    await ctx.channel.send(user.avatar)

bot.run(TOKEN)
