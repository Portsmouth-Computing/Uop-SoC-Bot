import discord

class CommandHandler:
    async def handle(self, bot: discord.Client, channel: discord.Channel, command: str, args: [str]):
        #Default/basic commands
        await bot.send_message(channel, command + command)