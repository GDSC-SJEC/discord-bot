import discord
import dotenv
import os



dotenv_file = os.path.join(os.curdir, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
else:
    print('Set env file with token before moving forward')
    exit(0)

# SETTING UP CLASS FOR DISCORD CLIENT
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged in as', self.user)



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents, prefix='$')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hello' in message.content.lower():
        await message.channel.send(f'Hello {message.author.name}, Welcome to GDSC SJEC')

    if message.content.startswith('$join'):
        await message.channel.send('Which Domain you wanna join?\n 1. Web Development\n 2. Mobile App Development\n 3. Game Development\n 4. AI/ML\n 5. Cloud Computing\n 6. Competitive Programming\n 7. UI/UX\n 8.Others')



client.run(os.environ['token'])