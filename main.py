import discord
from discord import app_commands
from discord.ext import commands
from tdkwrapper import tdkresponse
from dotenv import load_dotenv
import os


Bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

@Bot.event
async def on_ready():
    """When the bot gets ready sync the commands."""
    print("Bot is ready.")
    try:
        await Bot.tree.sync()
    except Exception as command_sync_error:
        print("Komutlar senkronize edilemedi", command_sync_error)

@Bot.tree.command(name="tdk", description="İstesiğiniz kelime'nin anlamını öğrenin.")
@app_commands.describe(kelime="Hangi kelime'nin anlamını öğrenmek istersiniz?")
async def tdk(interaction: discord.Interaction, kelime: str):
    await interaction.response.send_message(
        embed=discord.Embed(
        title="TDK Sorgu",
        description=f"> {kelime}",
        )
    )
    await interaction.followup.send(
        wait=True,
        embed=discord.Embed(
        title="Kelime Anlam",
        description=tdkresponse(kelime),
        )
    )

Bot.run(BOT_TOKEN)