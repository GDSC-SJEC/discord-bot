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
        super().__init__(command_prefix='~', intents = discord.Intents.all())
        self.message_content = True
        self.members = True
        # self.guilds = True

    async def on_ready(self):
        print('Logged in as', self.user)
        # self.add_view(verify_button_view())
        # self.add_view(form_button_view())

    # async def setup_hook(self):
    #     await self.tree.sync()
    #     print(f"Synced slash commands for {self.user.name}")

    async def on_command_error(self, ctx, error):
        print(error)
        await ctx.reply(error, ephemeral=True) # Dont print error in the discord channel

class verify_button_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "Verify yourself", style = discord.ButtonStyle.primary, custom_id = "verify", emoji = "❌")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):

        if 'verified' not in list(map(str,interaction.message.author.roles)):
            verifiedUser = discord.utils.get(interaction.guild.roles, name = 'verified')
            await interaction.user.add_roles(verifiedUser)
        else:
            await interaction.response.send_message(f"{interaction.user.mention} is already verified")

        button.label = "verified"
        button.emoji = "✅"
        button.disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"Thank you {interaction.user.mention}, You are now a verified user✅\n ```Now you can use ~joingdsc command to join your domain of interest!```")
        # await discord.Interaction.response.send_message(f"Thank you {interaction.user}, You are now a verified user✅\n ```Now you can use ~joingdsc command to join your domain of interest!```")


class form_button_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

        formButton = discord.ui.Button(label='GDSC FORM', style=discord.ButtonStyle.link, url='https://details.gdscsjec.in/')
        self.add_item(formButton)

    # @discord.ui.button(label = "FORM", style = discord.ButtonStyle.link)
    # async def form(self, interaction: discord.Interaction, button: discord.ui.Button):
    #     button.disabled = True
    #     await interaction.response.edit_message(view=self)
    #     await interaction.followup.send("Thank you for filling the form")


# class domainDropdown(discord.ui.View):
#     @discord.ui.select(
#         min_values = 1,
#         max_values = 2,
#         placeholder = "Choose a domain you would like to delve into!",
#         options = [
#             discord.SelectOption(
#                 label = "Web Development",
#                 description = "GDSC",
#                 emoji = "🌐"
#             ),
#             discord.SelectOption(
#                 label = "Mobile App Development",
#                 description = "GDSC",
#                 emoji = "📱"
#             ),
#             discord.SelectOption(
#                 label = "Game Development",
#                 description = "Get in the Game!",
#                 emoji = "🎮"
#             ),
#             discord.SelectOption(
#                 label = "AI/ML",
#                 description = "GDSC",
#                 emoji = "🤖"
#             ),
#             discord.SelectOption(
#                 label = "Cloud Computing",
#                 description = "GDSC",
#                 emoji = "☁️"
#             ),
#             discord.SelectOption(
#                 label = "Competitive Programming",
#                 description = "GDSC",
#                 emoji = "🏅"
#             ),
#             discord.SelectOption(
#                 label = "UI/UX Design",
#                 description = "GDSC",
#                 emoji = "🖼"
#             ),
#         ]
#     )

#     async def callback(self, interaction, select):
#         roles = {
#             "Web Development": "WEB",
#             "Mobile App Development": "MOBILE",
#             "Game Development": "GAME",
#             "AI/ML": "AI/ML",
#             "Cloud Computing": "CLOUD",
#             "Competitive Programming": "COMPETITIVE",
#             "UI/UX Design": "UI/UX"

#         }
#         for domain in select.values:
#             verifiedUser = discord.utils.get(interaction.guild.roles, name = roles[domain])
#             await interaction.user.add_roles(verifiedUser)
#         select.disabled = True
#         await interaction.response.edit_message(view=self)
#         await interaction.followup.send(f"Thank you 🥳\n You have succesfully joined the following domains {select.values} ")

# class testModal(discord.ui.View):
#     def __init__(self):
#         super().__init__(timeout = None)

#     @discord.ui.modal(title = "test Modal", custom_id = "mod01")
#     async def modal(self, interaction: discord.Interaction, button: discord.ui.Button):
#         await interaction.response.send_message("Hello", view = testModal())

    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot = MyClient()
# bot.remove_command('help')
# tree = app_commands.CommandTree(bot)

domains = ['Web Development', 'Mobile App Development', 'Game Development', 'AI/ML', 'Cloud Computing', 'Competitive Programming',  'UI/UX']
roles = ['WEB', 'MOBILE', 'GAME', 'AI/ML', 'CLOUD', 'COMPETITIVE', 'UI/UX']
roles = {
            "Web Development": "WEB",
            "Mobile App Development": "MOBILE",
            "Game Development": "GAME",
            "AI/ML": "AI/ML",
            "Cloud Computing": "CLOUD",
            "Competitive Programming": "COMPETITIVE",
            "UI/UX Design": "UI/UX"
        }


# bot = commands.Bot(command_prefix='!', intents = discord.Intents.default())

# @bot.command(name='verify button', description='just a verify button')
# async def button(interaction: discord.Interaction):
#     await interaction.reply('Please Verify before youself before you can join any domain!')
#     await interaction.send(view = verify_button_view())

@bot.hybrid_command(name = 'ping', with_app_command = True)
async def pinging(ctx):
    await ctx.reply('Pong~')

# @bot.command()
# async def test(ctx, *args):
#     # print("firing this")
#     arguments = ', '.join(args)
#     # print(arguments[5])
#     await ctx.reply(f'{len(args)} arguments: {arguments}')

@bot.command()
async def join(ctx):
    # await ctx.reply(f'Which Domain you wanna join?\n 1. Web Development\n 2. Mobile App Development\n 3. Game Development\n 4. AI/ML\n 5. Cloud Computing\n 6. Competitive Programming\n 7. UI/UX\n 8.Others')
    # await ctx.send('```Use ~joingdsc [domain index] command to join any of the above domains```')
    embed = discord.Embed(color = 1, title = 'Verification Needed', description = 'Please Verify before youself before you can join any domain!')
    await ctx.send(embed = embed, view = verify_button_view())


@bot.hybrid_command(name = 'joingdsc', with_app_command = True)
# @commands.has_role("GDSC-SJEC") 
async def joingdsc(ctx):
    try:
        userCurrentRole = list(map(str,ctx.author.roles))
        print(userCurrentRole)

        # if len(userCurrentRole) > 4:
        #     await ctx.reply(f'You have reached your maximum level of domains!\n Contact Admin for Help 🤗', ephemeral=True)
        #     return

        if 'verified' not in userCurrentRole:
            await ctx.reply('Please verify yourself before joining any domain!')
            return

        # domain = domains[int(index)-1]   
        
        # member = ctx.author
        # var = discord.utils.get(ctx.guild.roles, name = roles[int(index)-1])
        # await member.add_roles(var)

        # await ctx.reply(f'Congratulations 🎉🎊,\nYou have Succesfully joined {domain}')

        # await ctx.send(view = domainDropdown())
        await ctx.send("Please go the #join channel and react to your interested Domain")

    except Exception:
        await ctx.reply(f'＞︿＜')

@bot.hybrid_command(name = 'gdsc', with_app_command = True)
async def gdsc(ctx):
    await ctx.reply('Avilable Commands are: \n```2. ~join\n3. ~gdsc \n4. ~ping```')
    # await discord.Interaction.response.send_message(view = button_view())

@bot.hybrid_command(name = 'verify', with_app_command = True)
async def verify(ctx):
    await ctx.reply(view = verify_button_view())


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # if 'hello' in message.content.lower() or 'hi' in message.content.lower():
    if message.content.lower().startswith('hi'):
        view = form_button_view()
        await message.author.send(view = view)
        await message.channel.send(f'Hello {message.author.mention} (👉ﾟヮﾟ)👉,\n Wassup\n Ive slided into your DMs, catch me there! 🤗')
        embed = discord.Embed(color = 0xffffff, title = 'The Process Flow', description = "Here's the step by step guide on what to do next")
        embed.add_field(name="Step 1", value="Check you DM for message from GDSC-SJEC BOT", inline=False)
        embed.add_field(name="Step 2", value="Click on the Button to store your info into our Database", inline=False)
        embed.add_field(name="Step 3", value="Go to _Introduction_  Channel and introduce yourself", inline=False)
        embed.add_field(name="Step 4", value="Come back to verification Channel and use ~join command", inline=False)
        # embed.add_field(name="You are good to go now!", value = '', inline=False)
        await message.author.send(embed = embed)

    if message.content.lower().startswith('domains'):
        # embed = discord.Embed(color = 0xff00ff, title = 'Web Development', description = "Web Dev is sexy profession")
        # embed.set_footer(text = "For more information contact the domain lead by clicking the name above")
        # embed.set_image(url = "https://picsum.photos/800/200?random=1")
        # embed.set_author(name = "godey", url = "https://www.google.com", icon_url = "https://www.google.com")

        domains = [
            {
                'color' : 0xffffff,
                'title' : 'Web Development',
                'description' : 'Game Development is also sexy',
                'footer' : {'text' : 'For more information contact the domain lead by clicking the name above'},
                'image' : {'url' : 'https://picsum.photos/800/200?random=2', 'height' : 200, 'width' : 800},
                'author' : {'name' : 'ashish', 'url' : 'https://www.google.com', 'icon_url' : 'https://www.google.com'}
            },
            {
            'color' : 0xffffff,
            'title' : 'Game Development',
            'description' : 'An art of developing a virtual world which models by the rules and constraints defined by you.',
            'footer' : {'text' : 'If you want to know more about Game Dev or have some doubts , you can always ping me by clicking on my name!'},
            'image' : {'url' : 'https://imgur.com/b3CirLf', 'height' : 200, 'width' : 800},
            'author' : {'name' : 'Ashish Kishore', 'url' : 'https://www.linkedin.com/in/ashish-kishore-kumar/', 'icon_url' : 'https://imgur.com/a/SkEI7kU' }
            },
            {
                'color' : 0xff09ff,
                'title' : 'Mobile App Development',
                'description' : 'Game Development is also sexy',
                'footer' : {'text' : 'For more information contact the domain lead by clicking the name above'},
                'image' : {'url' : 'https://picsum.photos/800/200?random=2', 'height' : 200, 'width' : 800},
                'author' : {'name' : 'ashish', 'url' : 'https://www.google.com', 'icon_url' : 'https://www.google.com'}
            }
        ]
        for dic in domains:
            embed = discord.Embed().from_dict(dic)
            await message.channel.send(embed = embed)


    # if message.content.startswith('$join'):
        # await message.channel.send('Which Domain you wanna join?\n 1. Web Development\n 2. Mobile App Development\n 3. Game Development\n 4. AI/ML\n 5. Cloud Computing\n 6. Competitive Programming\n 7. UI/UX\n 8.Others')
    
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    await message.channel.send(f'Yo {message.member.name}, Admin saw what you deleted 😏')

@bot.event 
async def on_member_join(member):
    print(member.roles)
    await member.send(f'Welcome {member.mention} to the GDSC Discord Server 🥳\n We are delighted to Have you here')

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.name == 'testing':
        try:
            reacted = discord.utils.get(reaction.message.guild.roles, name = roles[reaction.message.embeds[0].title])
            await user.add_roles(reacted)
            await user.send(f"You are now a part of the {reaction.message.embeds[0].title} Domain of GDSC-SJEC community 🥳")
        except IndexError:
            await user.send("Oh Sorry!, You reacted to wrong message 😕")



bot.run(os.environ['token'])