import discord
import command_handler as cmd

async def handle_message_event(bot: discord.Client, message: discord.Message):
    content = message.content
    channel = message.channel
    #The "!" character in a mesage indicates it is a command
    if content.startswith("!"):
        content = content[1:]
        args    = content.split(" ")
        command = args[0]
        await cmd.handle_command(bot, channel, command, args)
