import discord
from command_handler import CommandHandler

class MessageEventHandler:
    def __init__(self):
        self.command_handler = CommandHandler()

    async def handle(self, bot: discord.Client, message: discord.Message):
        content = message.content
        channel = message.channel
        #The "!" character in a mesage indicates it is a command
        if content.startswith("!"):
                content = content[1:]
                args    = content.split(" ")
                command = args[0]
                await self.command_handler.handle(bot, channel, command, args)
        