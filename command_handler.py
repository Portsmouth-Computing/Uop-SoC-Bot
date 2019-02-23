import discord

async def handle_command(bot: discord.Client, channel: discord.Channel, command: str, args: [str]):
    await bot.send_message(channel, command + command)