from dotenv import load_dotenv
load_dotenv()
import os
import discord
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class NovorizontinoBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = NovorizontinoBot()

@bot.event
async def on_ready():
    print(f"🐯 {bot.user} está online!")
    print("NOVORIZONTINO BOT iniciado!")

@bot.tree.command(name="ping", description="Verifica se o bot está funcionando")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🐯 O NOVORIZONTINO BOT está na área! 💛🖤"
    )

@bot.tree.command(name="novorizontino", description="Saudação da torcida")
async def novorizontino(interaction: discord.Interaction):
    await interaction.response.send_message(
        "💛🖤 Aqui é Novorizontino! "
        "A força do Tigre vem da sua torcida! 🐯"
    )

if not TOKEN:
    raise RuntimeError("Configure a variável DISCORD_TOKEN!")

bot.run(TOKEN)
