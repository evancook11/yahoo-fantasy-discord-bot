from pathlib import Path
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from yahoo_api import YahooApi
from img_generator import create_html_table, html_to_image
import formatting

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
league_id = os.getenv("YAHOO_LEAGUE_ID")

if not discord_token:
    print("No discord token configured")
    exit()

if not league_id:
    print("No league id given")
    exit()


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

yahoo_api = YahooApi(league_id, "nhl", Path(__file__).parent)

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
    standings = yahoo_api.getLeagueStandings()
    html_content = create_html_table(standings)
    img = html_to_image(html_content)
    discord_img = discord.File(img)
    await interaction.response.send_message(file=discord_img)

bot.run(discord_token)
