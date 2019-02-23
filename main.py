import discord
import json

bot = discord.Client()
with open("config.json") as file:
    config = json.load(file)

@bot.event
async def on_ready():
    print("Bot is now active")

bot.run(config["id"])