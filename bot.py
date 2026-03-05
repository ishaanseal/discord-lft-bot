import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="-", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "-lft":
        await message.create_thread(
            name=f"LFT - {message.author.name}",
            auto_archive_duration=60
        )
        await message.delete()

    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))
