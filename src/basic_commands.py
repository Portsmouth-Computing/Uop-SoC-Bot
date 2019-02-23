import discord 
import json

from command import Command

class BasicCommandHandler:
    '''Commands that are simple and do not require a prefix'''
    def __init__(self):
        self.name = "Basic"
        self.basic_commands = [
            Command("source", ">source", "Gets a link to the source code of this bot", "https://github.com/Portsmouth-Computing/Uop-SoC-Bot")
        ]
        self.commands = [
           Command("deadline", ">deadline inse", "Gets all deadlines for a module", deadline),
           Command("exam", ">exam inse", "Gets the Exam/ Coursework weighting split for a module", exam) 
        ]

    async def try_execute(self, bot, channel, command, args):
        '''Attempts to execute a command, if it exists. Returns false if a command does not exist'''
        #TODO Generalise these loops somehow
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
        

def get_course_info(detail, unit):
    '''Gets basic info for a unit based on the detail, eg deadline or exam'''
    with open("data/course_info.json") as file:
        info = json.load(file)[detail]
    if unit in info:
        return info[unit]
    return None

async def deadline(bot, channel, command, args):
    '''Command function for getting the coursework deadline dates for a module'''
    unit = args[0] 
    deadlines = get_course_info("deadlines", unit)
    if deadlines:
        output = discord.Embed() 
        output.title = "Deadlines for unit: " + unit.upper()
        for dl in deadlines:
            output.add_field(name = "Name: " + dl[0], value = "Deadline: " + dl[1])
        await bot.send_message(channel, embed = output)

async def exam(bot, channel, command, args):
    '''Command function for getting the coursework/ exam split of a module'''
    unit = args[0] 
    exams = get_course_info("exams", unit)
    if exams:
        output = discord.Embed() 
        output.title = "Exam/Coursework split for unit: "  + unit.upper()
        output.add_field(name = "Exam",         value = str(exams["ex"]) + "%", inline = True)
        output.add_field(name = "Coursework",   value = str(exams["cw"]) + "%", inline = True)
        await bot.send_message(channel, embed = output)

        