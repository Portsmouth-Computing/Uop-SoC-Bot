import json
import discord
import os
import time
import random

_XP     = "xp"
_NEXT   = "next"
_TOTAL  = "total"
_LEVEL  = "level"
_TIME   = "time"

def _init_user(id, data):
    data[id] = {}
    data[id][_XP]     = 0
    data[id][_NEXT]   = 50
    data[id][_TOTAL]  = 0
    data[id][_LEVEL]  = 0
    data[id][_TIME]   = 0

async def update(bot, channel, member, message):
    levels = load_levels()
    if not member.id in levels:
        _init_user(member.id, levels)

    user = levels[member.id]

    #Check for the cooldown as there msut be a minimum 25s gap between messages
    #to actually gain xp to avoid spam
    now = int(time.time())
    stamp = user[_TIME]
    if now - stamp > 25:
        #Do the level system stuff
        user[_TIME] = now
        xp_gain     = random.randrange(10, 20)
        user[_XP]    += xp_gain
        user[_TOTAL] += xp_gain
        #Level up
        if user[_XP] > user[_NEXT]:
            user[_XP] -= user[_NEXT]
            next_level = int(user[_NEXT] * 1.5)
            user[_NEXT] = next_level
            user[_LEVEL] += 1
            await bot.send_message(channel, "Congrats " + member.name + "! You have leveled up to level " + str(user[_LEVEL]))
    save_levels(levels)

def load_levels():
    with open("data/levels.json", "r") as file:
        return json.load(file)

def save_levels(data):
    with open("data/levels.json", "w") as file:
        json.dump(data, file)