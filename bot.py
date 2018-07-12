# REFERENCES:
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
# https://discordpy.readthedocs.io/en/latest/api.html?highlight=event%20reference
# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

import discord
print(discord.__version__)

TOKEN = 'NDY2MTExMDExNTY5Nzk1MDgy.DiXTRA.E2yeF9I-Bx2DcHzUgxqWTbcOM_o'

client = discord.Client()

def roles_list(author):
    roles_str = ""
    for i in range(1, len(author.roles)):
        roles_str += author.roles[i].name
        if i != (len(author.roles) - 1):
            roles_str += ", "
    return roles_str

def embed_creator(message, channel):
##    confine = discord.Embed(title = "confine {} to {}",
##                             description = "a list of helpful commands!",
##                             color = 0xee4000)
##        bothelp.set_author(name="houndour",
##                           icon_url = "https://img.pokemondb.net/sprites/heartgold-soulsilver/back-normal/houndour.png")
##        bothelp.add_field(name = "h.info",
##                          value = "gives bot description",
##                          inline = False)
##        bothelp.add_field(name = "h.help",
##                          value = "lists commands",
##                          inline = False)
##        bothelp.add_field(name = "h.hint",
##                          value = "lists channel-specific hints",
##                          inline = False)
##        bothelp.add_field(name = "h.test", value = "says hello!",
##                          inline = False)
    pass

@client.event
async def on_message(message):

    lust_role = discord.utils.get(message.guild.roles, name = "Big Sexy")
    greed_role = discord.utils.get(message.guild.roles, name = "capitalist")
    anger_role = discord.utils.get(message.guild.roles, name = "Big Mad")
    hellion_role = discord.utils.get(message.guild.roles, name = "hellion")
    bokrae_role = discord.utils.get(message.guild.roles, name = "bokrae ;)")

    bot_garden = discord.utils.get(message.guild.channels, name = "bot-garden-of-eden")
    
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #test
    if message.content.startswith('h.test'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    #info
    elif message.content.startswith('h.info'):
        
        info = discord.Embed(title = "houndour_bot",
                              description = "a friendly helper hellhound. message h.help for more info!",
                              color = 0xee4000)
        info.set_author(name = "houndour",
                        icon_url="https://img.pokemondb.net/sprites/heartgold-soulsilver/back-normal/houndour.png")
        info.add_field(name = "author", value = "@mystery vidya#4762",
                       inline = False)
        info.add_field(name = "warning", value = "a bot with role management and mod functions. ONLY for use within mystery-vidya's hell server. some of its functions are prompted upon normal messaging activity within the server. ping vidya if you have any questions about this bot.")
        
        await message.channel.send("", embed = info)

    #help
    elif message.content.startswith('h.help'):

        bothelp = discord.Embed(title = "help",
                             description = "a list of helpful commands!",
                             color = 0xee4000)
        bothelp.set_author(name="houndour",
                           icon_url = "https://img.pokemondb.net/sprites/heartgold-soulsilver/back-normal/houndour.png")
        bothelp.add_field(name = "h.info",
                          value = "gives bot description",
                          inline = False)
        bothelp.add_field(name = "h.help",
                          value = "lists commands",
                          inline = False)
        bothelp.add_field(name = "h.hint",
                          value = "lists channel-specific hints",
                          inline = False)
        bothelp.add_field(name = "h.test", value = "says hello!",
                          inline = False)

        await message.channel.send("", embed = bothelp)

    #hint
    elif message.content.startswith('h.hint'):
        if message.channel.name == "limbo":
            await message.channel.send("hint: the mods are here if you need any help.")
        elif message.channel.name == "lust":
            await message.channel.send("hint: an ace is as an ace does.")
        elif message.channel.name == "gluttony":
            await message.channel.send("hint: anything can be a hot dog if you put enough ketchup on it.")
        elif message.channel.name == "greed":
            await message.channel.send("hint: i can show you your heart's desire...")
        elif message.channel.name == "anger":
            await message.channel.send("hint: let out your anger! catharsis is good for the soul.")
        elif message.channel.name == "heresy":
            await message.channel.send("hint: there is no god here, only the laws of the internet.")
        elif message.channel.name == "violence":
            await message.channel.send("hint: what a curious role name, wouldn't you say?")
        elif message.channel.name == "fraud":
            await message.channel.send("hint: stuck, are you? pity.")
        elif message.channel.name == "treachery":
            await message.channel.send("hint: it's time for you all to turn on each other. or something like that.")
        elif message.channel.name == "throne-room":
            await message.channel.send("https://www.youtube.com/watch?v=1Bix44C1EzY")
        else:
            await message.channel.send("this channel does not have a set hint. try asking a mod for help.")

    #granting roles - only for hellions
    elif hellion_role in message.author.roles and message.channel.name != "nsfw":

        #limbo - mentioning a mod's name or @ing a mod in limbo
        mod_names = ["vidya", "loki", "atriel", "atty"]
        mod_userids = ["magnetowasright", "mystery vidya", "Atriel"]

        if message.channel.name == "limbo":
            for i in range(0, len(mod_names)):
                if mod_names[i] in message.content.lower():
                    await message.author.add_roles(lust_role)
                    break
                
            if len(message.mentions) > 0:
                for person in message.mentions:
                    if person.name in mod_userids:
                        await message.author.add_roles(lust_role)
                        break

            elif len(message.role_mentions) > 0:
                for rolex in message.role_mentions:
                    if rolex.name == "vergil":
                        await message.author.add_roles(lust_role)
                        break

        #greed - using "want" in greed
        if "want" in message.content.lower() and message.channel.name == "greed":
            await message.author.add_roles(greed_role)

        #anger - using more than three exclamation points or question marks in a row
        if message.channel.name == "anger":
            if "???" in message.content.lower() or "!!!" in message.content.lower():
                await message.author.add_roles(anger_role)

            capscount = 0    
            for i in range(0, len(message.content)):
                if message.content[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    capscount += 1
                if capscount > 9:
                    await message.author.add_roles(anger_role)
                    break
                
    #HOW TO GET STUCK (also only for hellions)
        #limbo - saying a circle name
        limbo_list = ["limbo", "lust", "gluttony", "greed", "anger", "heresy", "violence", "fraud", "treachery"]
        for i in range(0, len(limbo_list)):
            if limbo_list[i] in message.content.lower():
                await bot_garden.send("**{}** should be confined to limbo. \n**current roles:** {}. \n**offending message:** {}".format(message.author.name, roles_list(message.author), message.content.strip()))
                break

        #lust - "sin bin", "lobster", "coconut"
        if "sin bin" in message.content.lower() or "coconut" in message.content.lower():
            await bot_garden.send("**{}** should be confined to lust. \n**current roles:** {}. \n**offending message:** {}".format(message.author.name, roles_list(message.author), message.content.strip()))

        #anger - cursing
        curse_list = ["heck", "shit", "bitch", "dick", "crap", "ass", "arse", "cock", "wank"]
        for i in range(0, len(curse_list)):
            if curse_list[i] in message.content.lower():
                await bot_garden.send("**{}** should be confined to anger. \n**current roles:** {}. \n**offending message:** {}".format(message.author.name, roles_list(message.author), message.content.strip()))
                break
        
        #heresy - using "god" or "hell"
        if "god" in message.content.lower() or "damn" in message.content.lower():
            await bot_garden.send("**{}** should be confined to heresy. \n**current roles:** {}. \n**offending message:** {}".format(message.author.name, roles_list(message.author), message.content.strip()))

        #fraud - "honest", "tbh"
        if "honest" in message.content.lower() or "tbh" in message.content.lower():
            await bot_garden.send("**{}** should be confined to fraud. \n**current roles:** {}. \n**offending message:** {}".format(message.author.name, roles_list(message.author), message.content.strip()))

        #treachery - "shame"
        if "sham" in message.content.lower():
            await bot_garden.send("**{}** should be confined to treachery. \n**current roles:** {}. \n**offending message:** {}".format(message.author.name, roles_list(message.author), message.content.strip()))

    #bokrae ;)
        if "lobster" in message.content.lower():
            await message.author.add_roles(bokrae_role)
            await bot_garden.send("**{}** is a lobster sympathizer! \n**current roles:** {}. \n**offending message:** {}".format(message.author.name, roles_list(message.author), message.content.strip()))

@client.event
async def on_reaction_add(reaction, user):

    hellion_role = discord.utils.get(reaction.message.guild.roles, name = "hellion")
    observer_role = discord.utils.get(reaction.message.guild.roles, name = "observer")
    violence_role = discord.utils.get(reaction.message.guild.roles, name = u"\U0001F52A"	u"\U0001F52A"	u"\U0001F52A")

    bot_garden = discord.utils.get(reaction.message.guild.channels, name = "bot-garden-of-eden")
    
##    #hellions vs. observers
##    if reaction.message.channel.name == "rules":
##        if reaction.emoji == u"\U0001F525":
##            await user.add_roles(hellion_role)
##        elif reaction.emoji == 	u"\U0001F440":
##            await user.add_roles(observer_role)

    if hellion_role not in user.roles:
        return
    
    #violence - emoji reacts        
    elif reaction.message.channel.name == "violence":
        await user.add_roles(violence_role)

#violence stuckitude - emoji reacts outside of violence 
    elif reaction.message.channel.name != "violence":
        await bot_garden.send("**{}** should be confined to violence. \n**current roles:** {}. \n**offending message:** {}".format(message.author.name, roles_list(message.author), message.content.strip()))
    
                
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
