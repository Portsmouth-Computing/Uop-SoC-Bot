import discord

from command import Command

class CommandHandler:
    def __init__(self):
        self.command_handlers = [BasicCommandHandler()]

    async def handle(self, bot: discord.Client, channel: discord.Channel, command: str, args: [str]):
        #Help command
        if command == "help":
            output = discord.Embed()
            output.title = "UoP Bot Help"
            for handler in self.command_handlers:
                for command in handler.basic_commands:
                    val =  "Description: " + command.description + "\n"
                    val += "Example: " + command.example
                    output.add_field(name = command.name, value = val)
            await bot.send_message(channel, embed = output)
            return

        #Other commands
        for handler in self.command_handlers:
            if await handler.try_execute(bot, channel, command, args):
                return

class BasicCommandHandler:
    def __init__(self):
        self.name = "Basic"
        self.basic_commands = [
            Command("source", ">source", "Gets a link to the source code of this bot", "https://github.com/Portsmouth-Computing/Uop-SoC-Bot")
        ]

    async def try_execute(self, bot: discord.Client, channel: discord.Channel, command: str, args: [str]):
        print("TRYING")
        for cmd in self.basic_commands:
            print (">" + command + "< >" + cmd.name + "<")
            if (cmd.name == command):
                await bot.send_message(channel, cmd.output)
