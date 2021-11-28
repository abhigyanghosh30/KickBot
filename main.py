import discord
import os
import datetime
from pymongo import MongoClient
from discord.ext import tasks


def read_token():
    with open('.env', 'r') as f:
        lines = f.readlines()
        # print(lines[0])
        return lines[0].strip(), lines[1].strip()


TOKEN, CONNECTION_STRING = read_token()
print(CONNECTION_STRING)

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)
dbclient = MongoClient(CONNECTION_STRING)
dbname = dbclient["KickBot"]
entry = {"username": "abhigyanghosh30", "time": 6}
dbname["user_list"].insert_one(entry)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

# @client.event
# async def on_member_join(member):
#   print(member.id)
#   db[member.id]=6
#   channel = discord.utils.get(client.get_all_channels(), guild__name='Wogharts', name='general')
#   await channel.send(member.name+" joined for 6 months")

# @client.event
# async def on_message(message):
#   msg = message.content
#   if msg.startswith("$set"):
#     k = msg.split()[1]
#     v = msg.split()[2]
#     member = discord.utils.find(lambda m: m.name == k, client.get_all_members())
#     db[str(member.id)]=v
#     await message.channel.send(k+" set to be banned "+v+" months from now")

# @client.event
# async def on_member_remove(member):
#   if member.id in db.keys():
#     del db[str(member.id)]

# @tasks.loop(hours=12)
# async def checkMembers():
#   print(db.keys())
#   n = datetime.datetime.now()
#   members = client.get_all_members()
#   for cl in members:
#     print(cl.id)
#     if str(cl.id) in db.keys():
#       print(cl.name)
#       j = cl.joined_at
#       tot = (n.year-j.year)*12+(n.month-j.month)
#       if tot>int(db[str(cl.id)]):
#         await cl.kick()

# keep_alive()
# checkMembers.start()
client.run(TOKEN)
