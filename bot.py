"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# MACIANAUTILITIES V2 - STABLE BRANCH V2.0.0
# By saying "client" I'm referring to it's bot instance.
# © 2021, contact@maciana.pl

# Dependencies import

import discord
from discord.appinfo import AppInfo
from discord.ext import commands
import asyncio
from datetime import datetime
import pprint
import time
import json
import os

# Client configuration

client = commands.Bot(command_prefix = '.')
client.launch_time = datetime.utcnow()
# (WILL USE IT LATER) config = open('config.json',)
# (WILL USE IT LATER) data = json.load(config)
ownerID = '418777009502552086'
# SECRET: Client's token
# Below is the bot's token you got while creating it's application.
# Anyone having this token can start and use your bot!
TOKEN = 'TOKEN'



# Successful startup notice

@client.event
async def on_ready():
    print (f'MacianaUtilities V2.0.0 STABLE >> The bot is ready, logged in as: {client.user} (ID: {client.user.id})')

# You can set up the bot's token in the "Client configuration section"

client.run(TOKEN)
