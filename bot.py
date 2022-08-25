import discord
from discord.ext import commands
from discord.utils import get
import dotenv
import os



dotenv_file = os.path.join(os.curdir, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
else:
    print('Set env file with token before moving forward')
    exit(0)

# SETTING UP CLASS FOR DISCORD CLIENT
class MyClient(commands.Bot):

    def __init__(self) -> None:
        super().__init__(command_prefix='!', intents = discord.Intents.all())
        self.message_content = True
        self.members = True
        # self.guilds = True

    async def on_ready(self):
        print('Logged in as', self.user)





client = MyClient()



# bot = commands.Bot(command_prefix='!', intents = discord.Intents.default())

@client.command()
async def test(ctx, *args):
    # print("firing this")
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

@client.command()
async def join(ctx):
    await ctx.send('Which Domain you wanna join?\n 1. Web Development\n 2. Mobile App Development\n 3. Game Development\n 4. AI/ML\n 5. Cloud Computing\n 6. Competitive Programming\n 7. UI/UX\n 8.Others')

@client.command()
async def gdsc(ctx):
    await ctx.send('```Avilable Commands are: \n1. !test\n2. !join\n3. !gdsc```')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hello' in message.content.lower():
        await message.channel.send(f'Hello {message.author.name} (👉ﾟヮﾟ)👉,\n Wassup, You can type !gdsc to see the available commands')

    # if message.content.startswith('$join'):
        # await message.channel.send('Which Domain you wanna join?\n 1. Web Development\n 2. Mobile App Development\n 3. Game Development\n 4. AI/ML\n 5. Cloud Computing\n 6. Competitive Programming\n 7. UI/UX\n 8.Others')
    
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    await message.channel.send(f'Yo {message.author.name}, Admin saw what you deleted 😏')

@client.event 
async def on_member_join(member):
    print(member.roles)
    await member.send(f'Welcome {member.name} to the GDSC Discord Server 🥳')




client.run(os.environ['token'])