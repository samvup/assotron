#assotron version 0.0.0.2 pre alpha
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("I may technically be half Butt and half robot, but im still Butter than you")
    await client.change_presence(game=discord.Game(name="Playing with Butts B)"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Butt":
        await client.send_message(message.channel, "Did someone summon me?")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "assotron yes":
        await client.send_message(message.channel, "You're welcome bb ;)")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "assotron no":
        await client.send_message(message.channel, "I'm doing my best okay... :(")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "assotron what":
        await client.send_message(message.channel, "heh... um... :/")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "assotron pls":
        await client.send_message(message.channel, "okay bb UwU")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "ass":
        await client.send_message(message.channel, "yes pls UwU")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "buttsbot":
        await client.send_message(message.channel, "...why are you talking about my dad?...")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "samvup":
    await client.send_message(message.channel, "Aye I know that guy! B)")

client.run(INSERT_TOKEN_HERE)
