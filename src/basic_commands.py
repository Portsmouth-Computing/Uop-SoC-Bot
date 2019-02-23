import discord 
import json

from command import Command

class BasicCommandHandler:
    def __init__(self):
        self.name = "Basic"
        self.basic_commands = [
            Command("source", ">source", "Gets a link to the source code of this bot", "https://github.com/Portsmouth-Computing/Uop-SoC-Bot")
        ]
        self.commands = [
           Command("deadline", ">deadline inse", "Gets all deadlines for a module", deadline) 
        ]

    async def try_execute(self, bot: discord.Client, channel: discord.Channel, command: str, args: [str]):
        #TODO Generalise this
        for cmd in self.basic_commands:
            if (cmd.name == command):
                await bot.send_message(channel, cmd.output)
        for cmd in self.commands:
            if (cmd.name == command):
                args = args[1:]
                await cmd.output(bot, channel, command, args)

def get_course_info():
    with open("data/course_info.json") as file:
        info = json.load(file)
    return info

async def deadline(bot: discord.Client, channel: discord.Channel, command: str, args: [str]):
    if len(args) < 1: 
        return
    unit = args[0] 
    deadlines = get_course_info()["deadlines"]
    if unit in deadlines:
        deadlines = deadlines[unit]
        output = discord.Embed() 
        output.title = "Deadlines for course: " + unit.upper()
        for dl in deadlines:
            output.add_field(name = "Name: " + dl[0], value = "Deadline: " + dl[1])
        await bot.send_message(channel, embed = output)