from unicodedata import name
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

    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral=True)





bot = MyClient()
domains = ['Web Development', 'Mobile App Development', 'Game Development', 'AI/ML', 'Cloud Computing', 'Competitive Programming',  'UI/UX']


# bot = commands.Bot(command_prefix='!', intents = discord.Intents.default())

@bot.hybrid_command(name = 'ping', with_app_command = True)
async def ping(ctx):
    await ctx.reply('Pong!')

@bot.command()
async def test(ctx, *args):
    # print("firing this")
    arguments = ', '.join(args)
    print(args[5])
    await ctx.reply(f'{len(args)} arguments: {arguments}')

@bot.command()
async def join(ctx):
    await ctx.reply(f'Which Domain you wanna join?\n 1. Web Development\n 2. Mobile App Development\n 3. Game Development\n 4. AI/ML\n 5. Cloud Computing\n 6. Competitive Programming\n 7. UI/UX\n 8.Others')
    await ctx.send('```Use !joingdsc [domain index] command to join any of the above domains```')

@bot.command()
async def joingdsc(ctx, index):
    try:
        if index == '8':
            await ctx.reply('Contact Admin for Assistance')
            return
        domain = domains[int(index)-1]
        await ctx.reply(f'Congratulations 🎉🎊,\nYou have Succesfully joined {domain}')
    except IndexError:
        await ctx.reply(f'Invalid Domain Index\n ＞︿＜')

@bot.command()
async def gdsc(ctx):
    await ctx.reply('Avilable Commands are: \n```1. !test\n2. !join\n3. !gdsc```')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'hello' in message.content.lower():
        await message.channel.send(f'Hello {message.author.name} (👉ﾟヮﾟ)👉,\n Wassup, You can type **!gdsc** to see the available commands')

    # if message.content.startswith('$join'):
        # await message.channel.send('Which Domain you wanna join?\n 1. Web Development\n 2. Mobile App Development\n 3. Game Development\n 4. AI/ML\n 5. Cloud Computing\n 6. Competitive Programming\n 7. UI/UX\n 8.Others')
    
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    await message.channel.send(f'Yo {message.author.name}, Admin saw what you deleted 😏')

@bot.event 
async def on_member_join(member):
    print(member.roles)
    await member.send(f'Welcome {member.name} to the GDSC Discord Server 🥳')




bot.run(os.environ['token'])