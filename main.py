from pathlib import Path
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from yahoo_api import YahooApi
import formatting

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

if not discord_token:
    print("No discord token configured")
    exit()


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

yahoo_api = YahooApi("127288", "nhl", Path(__file__).parent)

@bot.event
async def on_ready():
    print("Bot is ready")
    try: 
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



@bot.tree.command(name="standings")
async def standings(interaction: discord.Interaction):
    response = formatting.formatStandings(yahoo_api.getLeagueStandings())
    await interaction.response.send_message(f"```\n{response}\n```")


bot.run(discord_token)
