import discord
import json

import message_event as MessageEvent

bot = discord.Client()

with open("config.json") as file:
    config = json.load(file)

@bot.event
async def on_ready():
    print("Bot is now active")

@bot.event
async def on_message(message):
    await MessageEvent.handle_message_event(bot, message)

bot.run(config["id"])