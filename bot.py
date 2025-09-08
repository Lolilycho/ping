import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # !ping の内容を読むのに必要

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # ms に変換
    await ctx.send(f"pong ({latency}ms)")

# トークンはハードコードせず環境変数から読み込む
import os
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
