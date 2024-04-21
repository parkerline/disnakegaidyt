import disnake; from disnake.ext import commands; from config import *
import os; import glob

bot = commands.Bot(
    command_prefix="!",
    test_guilds=[BOT["GUILD_ID"]],
    intents=disnake.Intents.all()
)
base_dir = os.path.dirname(os.path.abspath(__file__))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} запущен')

bot.run(BOT["TOKEN"])