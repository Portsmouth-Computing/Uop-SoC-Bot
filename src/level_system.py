import json
import discord
import os
import time
import random

XP     = "xp"
NEXT   = "next"
TOTAL  = "total"
LEVEL  = "level"
TIME   = "time"

def _init_user(id, data):
    data[id] = {}
    data[id][XP]     = 0
    data[id][NEXT]   = 50
    data[id][TOTAL]  = 0
    data[id][LEVEL]  = 0
    data[id][TIME]   = 0

async def update(bot, channel, member, message):
    levels = load_levels()
    if not member.id in levels:
        _init_user(member.id, levels)

    user = levels[member.id]

    #Check for the cooldown as there msut be a minimum 25s gap between messages
    #to actually gain xp to avoid spam
    now = int(time.time())
    stamp = user[TIME]
    if now - stamp > 25:
        #Do the level system stuff
        user[TIME] = now
        xp_gain     = random.randrange(10, 20)
        user[XP]    += xp_gain
        user[TOTAL] += xp_gain
        #Level up
        if user[XP] > user[NEXT]:
            user[XP] -= user[NEXT]
            next_level = int(user[NEXT] * 1.5)
            user[NEXT] = next_level
            user[LEVEL] += 1
            await bot.send_message(channel, "Congrats " + member.name + "! You have leveled up to level " + str(user[LEVEL]))
    save_levels(levels)

def load_levels():
    with open("data/levels.json", "r") as file:
        return json.load(file)

def save_levels(data):
    
    with open("data/levels.json", "w") as file:
        json.dump(data, file)