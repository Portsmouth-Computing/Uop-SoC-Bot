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
           Command("deadline", ">deadline inse", "Gets all deadlines for a module", deadline),
           Command("exam", ">exam inse", "Gets th exam/coursework weighting for a module", exam) 
        ]

    async def try_execute(self, bot, channel, command, args):
        #TODO Generalise this
        for cmd in self.basic_commands:
            if (cmd.name == command):
                await bot.send_message(channel, cmd.output)
                return True
        if len(args) < 1: 
            return False
        for cmd in self.commands:
            if (cmd.name == command):
                args = args[1:]
                await cmd.output(bot, channel, command, args)
                return True
        return False
        

def get_course_info():
    with open("data/course_info.json") as file:
        info = json.load(file)
    return info

async def deadline(bot, channel, command, args):
    unit = args[0] 
    deadlines = get_course_info()["deadlines"]
    if unit in deadlines:
        deadlines = deadlines[unit]
        output = discord.Embed() 
        output.title = "Deadlines for unit: " + unit.upper()
        for dl in deadlines:
            output.add_field(name = "Name: " + dl[0], value = "Deadline: " + dl[1])
        await bot.send_message(channel, embed = output)

async def exam(bot, channel, command, args):
    unit = args[0] 
    exams = get_course_info()["exams"]
    if unit in exams:
        exams = exams[unit]
        print(exams)
        output = discord.Embed() 
        output.title = "Exam/Coursework split for unit: "  + unit.upper()
        output.add_field(name = "Exam",         value = str(exams["ex"]) + "%", inline = True)
        output.add_field(name = "Coursework",   value = str(exams["cw"]) + "%", inline = True)
        await bot.send_message(channel, embed = output)

        