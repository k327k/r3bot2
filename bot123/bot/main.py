

import random
import discord
from discord.ext import commands
from discord.ext import tasks
from twitchAPI.twitch import Twitch
from twitch import checkIfLive


PREFIX = 'R3.'
INTENTS = discord.Intents().all()
bot = commands.Bot(command_prefix = PREFIX, intents = INTENTS)
zleslowa = ['nigger', 'czarnuch', 'żyd', 'kobieta', 'n1gger', 'nlgger','zyd','nigg3r','pedał','pedal','p3dał','p3dal', 'shiroi','shiroitenshi','pedofil','nigg','ambiwalen']
TOKEN = 'MTAyNDM0NjM3MzUxNDA4NDQ2Mw.GpWoYi.XYxylQXx-_UP3u-eHShf4IzL_GZe04UkzGgHio'
limit = 0


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Messages were cleared by  {}'.format(ctx.author.mention))
        await ctx.message.delete()

@bot.command()
async def helpadmin(ctx):
    embed = discord.Embed(
        title = 'Bot commands',
        description = "PREFIX: R3. \n-clear(number of messages to clear)\n there's no more commands currently sori",
        colour = discord.Colour.red()
    )

    embed.set_footer(text='Made by random guy')
    embed.set_author(name = 'R3VOLT ESPORTS', icon_url='https://cdn.discordapp.com/attachments/1000041926327799818/1022945082363609198/smok_r3_gotowy.png')

    await ctx.message.delete()
    await ctx.channel.send(embed=embed)
    

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Scrolling Twitter"))

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = 'Revolutionist')
    await member.add_roles(role)
    
@bot.event
async def on_message(message):

    
    if message.author.bot == False:
        role = discord.utils.find(lambda r: r.name != 'Anarchist', message.author.roles)
        if 'discord.gg' in message.content:
            if role in message.author.roles:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Why are u trying to advertise other discords ma boi?", delete_after=15)
        if 'piwo' in message.content:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Co? Piwo? A mogę też?")
        if message.channel.name != 'mountain-pl':
            if any(zleslowo in message.content.lower() for zleslowo in zleslowa):
                await message.delete()
                await message.channel.send(f"{message.author.mention} U are not allowed to use words like that", delete_after=15)

    await bot.process_commands(message)
    

    
@bot.event
async def on_message_edit(bmess, amess):
    if bmess.author.bot == False:
        if any(zleslowo in amess.content.lower() for zleslowo in zleslowa):
            await amess.delete()
            await amess.channel.send(f"{amess.author.mention} U ain't allowed to edit messages that are not kind :c", delete_after=15)


bot.run(TOKEN)

