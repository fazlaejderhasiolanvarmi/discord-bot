import discord

client = discord.Client()
token = ''

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>sa'):
        await message.channel.send('Ehlen ve sehlen kardeşim ase')
    elif message.content.startswith('>naber'):
        await message.channel.send('iisn')
    elif message.content.startswith('>kimsin'):
        await message.channel.send('Ben senim')
    elif message.content.startswith('>selami'):
        await message.channel.send('Akgün Selami')
    elif message.content.startswith('>'):
        await message.channel.send('ne diyon anlamıyom')

client.run(token)
