import discord
import json

from message_event import MessageEventHandler

bot = discord.Client()
message_event_handler = MessageEventHandler()

with open("config.json") as file:
    config = json.load(file)

@bot.event
async def on_ready():
    print("Bot is now active")
    game = discord.Game()
    game.name = "Type '>help'"
    await bot.change_presence(game = game)

@bot.event
async def on_message(message):
    await message_event_handler.handle(bot, message)

bot.run(config["id"])