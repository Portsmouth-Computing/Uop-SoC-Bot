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
            if await try_execute(handler, bot, channel, command, args):
                return

async def try_execute(command_handler, bot, channel, command, args):
    '''Attempts to execute a command, if it exists. Returns false if a command does not exist'''
    #TODO Generalise these loops somehow
    for cmd in command_handler.basic_commands:
        if (cmd.name == command):
            await bot.send_message(channel, cmd.output)
            return True
    if len(args) < 1: 
        return False
    for cmd in command_handler.commands:
        if (cmd.name == command):
            args = args[1:]
            await cmd.output(bot, channel, command, args)
            return True
    return False