import discord

from command import Command
from basic_commands import BasicCommandHandler

class CommandHandler:
    def __init__(self):
        self.command_handlers = [BasicCommandHandler()]

    async def handle(self, bot: discord.Client, channel: discord.Channel, command: str, args: [str]):
        #Help command
        if command == "help":
            output = discord.Embed()
            output.title = "UoP Bot Help"
            for handler in self.command_handlers:
                for command in handler.basic_commands + handler.commands:
                    val =  "Description: " + command.description + "\n"
                    val += "Example: " + command.example
                    output.add_field(name = command.name, value = val)
            await bot.send_message(channel, embed = output)
            return

        #Other commands
        for handler in self.command_handlers:
            if await handler.try_execute(bot, channel, command, args):
                return
