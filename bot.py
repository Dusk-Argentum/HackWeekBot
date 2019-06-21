import os

import discord

import asyncio
import aiohttp

from discord.ext import commands
from discord.ext.commands import CommandInvokeError

OWNER_ID = "97153790897045504"

PREFIX = "-"
DESCRIPTION = "A bot written by @Dusk-Argentum#6530 for Discord's Hack Week 2019."
TOKEN = os.environ.get("WOLFRAM")

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), description=DESCRIPTION, pm_help=True)
client = discord.Client()


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with Discord! | -help"), status=discord.Status("online"))


@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, CommandInvokeError):
        error = error.original
    await bot.send_message(ctx.message.channel, "Whoops! "+error)


@bot.command(pass_context=True)
async def remind(ctx, message: str, input: int):
    if input is None:
        await bot.say("Please input a time!")
    else:
        await bot.say("Reminder set for "+input+" seconds from now!")
        await asyncio.sleep(input)
        await bot.say(ctx.message.author.mention+": "+message)

bot.run(TOKEN)
