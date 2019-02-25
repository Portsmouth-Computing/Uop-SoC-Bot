import discord 
import json
import level_system as lvl_sys

from command import Command

class LevelCommandHandler:
    '''Commands to do with the leveling system'''
    def __init__(self):
        self.name = "Levels"
        self.basic_commands = []
        self.commands = [
            Command(
                "rank",     \
                ">rank",    \
                "Gets your level and exp info, as well as your rank", \
                rank),
        ]

async def rank(bot, channel, command, args, member):
    levels = lvl_sys.load_levels()
    user_levels = levels[member.id]
    output = discord.Embed()
    output.title = "Levels for user: " + member.name
    output.add_field(name = "Level", value = user_levels[lvl_sys.LEVEL])
    output.add_field(name = "Experience", value = user_levels[lvl_sys.XP])
    output.add_field(name = "Next Level", value = user_levels[lvl_sys.NEXT])
    output.add_field(name = "Total Experience", value = user_levels[lvl_sys.TOTAL])
    await bot.send_message(channel, embed = output)

    