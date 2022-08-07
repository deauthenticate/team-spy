import imghdr
import os
import sys
import asyncio
import random
import re
os.system("pip install discord")
##
#os.system("pip install git+https://github.com/Rapptz/discord.py")
os.system("pip install httpx")
import httpx
os.system("pip install aiohttp")
import aiohttp
from datetime import datetime
import datetime as datetime
from datetime import date
os.system("pip install date")
import time
#os.system("pip install random
# os.system("pip install -U git+https://github.com/Rapptz/discord.py")
os.system("pip install discord.py[voice]")
os.system("pip install dhooks")
import discord  
from dhooks import Webhook, Webhook
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
os.system('pip install jishaku')
import jishaku
os.system("pip install --upgrade discord-components")
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption



tkn = os.environ['noo']
prefix = "."
shards = 1
noprefix = 980720852440084540


def get_prefix(client, message): 
    role = discord.utils.get(message.guild.roles, id=980698747862392912)
    nopref = message.guild.get_role(noprefix)
    member = message.author
    if role in member.roles or nopref in member.roles:
   # if member.id == 921357941725093889:
      return (["-", "*","+", ".", ">", "?", ""])
    elif member.id == 661563598711291904:
      return (["-", "*","+", ".", ">", "?", ""])
   # elif message.author.id == 799927959569956904:
  #    return ""
   # elif message.author.id == 921357941725093889:
    #  return ""
    return (["-", "*","+", ".", ">", "?"])

intents = discord.Intents.all()
intents.members = True
intents.messages = True
headers = {'Authorization': f'Bot {tkn}'}
client = commands.AutoShardedBot(shard_count=shards, command_prefix=get_prefix, case_insensitive=True, intents=intents)
DiscordComponents(client)
client.remove_command('help')
#lash = SlashCommand(client, sync_commands=True)
#uttons = ButtonsClient(client)
hookshit = Webhook("https://discord.com/api/webhooks/937939926983536731/Dl2CcCTNqrCDLrAL0PBLaBkzLtrQOd5q30CRbylIkkY0Orc4rWcRWcPAB6krxXAUNdhj")
antialt = True
raidmode = False
client.load_extension('jishaku')


import ast
import inspect
import re

import discord


# s: https://medium.com/@chipiga86/python-monkey-patching-like-a-boss-87d7ddb8098e
def source(o):
    s = inspect.getsource(o).split("\n")
    indent = len(s[0]) - len(s[0].lstrip())
    return "\n".join(i[indent:] for i in s)


source_ = source(discord.gateway.DiscordWebSocket.identify)
patched = re.sub(
    r'([\'"]\$browser[\'"]:\s?[\'"]).+([\'"])',  # hh this regex
    r"\1Discord Android\2",  # s: https://luna.gitlab.io/discord-unofficial-docs/mobile_indicator.html
    source_
)

loc = {}
exec(compile(ast.parse(patched), "<string>", "exec"), discord.gateway.__dict__, loc)

discord.gateway.DiscordWebSocket.identify = loc["identify"]


#switchlol

logger_ = 978630297195266060
tagxd = "ˢᵖʸ"
official_sv = "https://discord.gg/sgeV3aUKcV"
everyoneid = 930307731166990347
guildid = 952495772073619466
guildname = "TEAM SPY"
pforp = False 
lockm = False
toprole = 963790605702561802
wallrole = 980698754527150080
secrole = 980698723397042206
vanitychan = "/gamer"
adminrole = 964483723770888193
statusded = "exploiting hell"
failedemo = "<a:spy_failed:980717989508825149>"
successemo = "<a:spy_success:980717907078172694>"
heartemo = ""
boostersid = 954586316987859005
announceschan = "・annc"
generalvc = "🍷・ LOUNGE"
voicerole = 980698728992215100
logschannel = 974709266588000256
randirole = 948249429859794946
nrskid = [f"<@&{randirole}>", "skids", "National Randi™", "Nangi Randi™", "2 rupaye ki Pepsi nangi randi sexi", "skids", "lmao ye wohi log hai jinhe spy roj chodta hai", "nr on my lund ke top", "Sasti Nangi Randi lode pe", "Nr ki maa ki chut maru?", "Nr ki maa ka bhosda faadu?"]
announceslock = False
wallrolename = "/"
muterole = 980698755638644806
risinplayzid = 661563598711291904
officialrole = 980698747862392912
quarantine = 980698724298805290
fansrole = 980725864742387712
girlfans = 980698750806802472
modsrole = 980698746616692776
adm1 = 980698727608123452
adm2  = 980698726559522847
vanitycode = "gamer"
securemode = 948563115111493672
console = 980698757593178172
msg = "・chat"
img = "・img"
cmd = "・cmds"
memes = "・memes"
msgid = 980780379181023262
cmdid = 980698738886586398
imgid = 980698737947058186
memesid = 980698739968704542
flmusicid = 980698744817352704
searchmid = 980698741902311474
logschann = 948202052201369610
muteid = 980698765142949918
rulesid = 980698732406398996
power = 980698725762609202

#colors

# g = client.get_guild(930307731166990347)
# red = discord.utils.get(g.roles, id=955433077772025896)
# black = discord.utils.get(g.roles, id=955433249184833576)
# blue = discord.utils.get(g.roles, id=955432936822407219)
# green = discord.utils.get(g.roles, id=955432794002182144)
# white = discord.utils.get(g.roles, id=955433186115080242)
# yellow = discord.utils.get(g.roles, id=955432734396911646)


#colors

@client.event
async def on_ready():
  now = datetime.datetime.utcnow()
  guild = client.get_guild(guildid)
  channel = discord.utils.get(client.get_all_channels(), name=vanitychan)
  #await guild.change_voice_state(channel=channel, self_mute=True, reason="24/7 vc.")
  await channel.connect()
  k = await guild.chunk()
  for m in k:
   if m.id == 925972299558060104:
      await m.edit(mute=True, reason="24/7 vc.")
  print('''
    Spy security is ready :P  
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P  
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P ''')

    
  #  members = 0
   # for guild in client.guilds:
     #   members += guild.member_count - 1

  await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.playing,
        name = f"{statusded}"
    ))
  code__ = await guild.vanity_invite()
  code_ = code__.code
  banlist = await guild.bans()
  banlen = len(banlist)
  h = httpx.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={now}")
  k = h.content.decode("utf-8")
  kk = k.replace('"', '')
  connect_ = int(kk)
  logger__ = discord.utils.get(client.get_all_channels(), id=logger_)
  admins_ = ""
  for mxd in guild.members:
  	if mxd.guild_permissions.administrator:
   	   admins_ += f"`-` {mxd.mention} - {mxd.id} - {mxd.name}#{mxd.discriminator}\n"
  mxbe = f'''>>> ___connected to websocket__,
proxy: non proxy connection,
shards: 1,
instances: 2,
threads: 404,
Api latency - 
instance 1 {client.latency},
instance 2 undefined,

__Guild info | Shard 0__
guild; "TEAM SPY",
guild_ban_length: {banlen},
vanity_url_code: "{code_}",
Under attack? : false

__Hosting:__
Platform : linux 
Provider :  heroku
Connected since : <t:{connect_}:R>

__Adminstrators: __
{admins_}'''
  embed = discord.Embed(color=00000, description=mxbe)
  await logger__.send(content="`•` https://discord.gg/spy .", embed=embed)
    
@client.event 
async def on_connect():
  global lockm
  time = datetime.datetime.now()
  today = date.today()
  remtime = today.strftime("%d/%m/%Y")
  lockmsg = "{} | Nightmode has been enabled | 9PM IST.".format(successemo)
  await client.wait_until_ready()
  guild = client.get_guild(930307731166990347)
  print("connected")
  # await asyncio.sleep(1)
  # while True:
  #   if lockm == False:
  #     if time.hour == 15 and time.minute == 42: # coz vro rdp ka time else 21= 9
  #       toprol = discord.utils.get(guild.roles, id=toprole)
  #       for dogla in list(guild.members):
  #         if dogla.bot:
  #           continue
  #         elif toprol in dogla.roles:
  #           try:
  #               await dogla.remove_roles(toprol, reason="Night Mode | 9PM IST")
  #           except:
  #               continue 
  #       lockm = True
  #       consolex = discord.utils.get(guild.channels, id=console)
  #       await consolex.send(lockmsg)
  #     lockm = False
  # await asyncio.sleep(1)
@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, CommandNotFound):
      return None
   # role = discord.utils.get(ctx.guild.roles, name="Nukers™")
   # member = ctx.message.author
  #  if role in member.roles:
    #  return None
   # if ctx.message.author.id == 799927959569956904:
   #   return None 
  #  elif ctx.message.author.id == 921357941725093889:
   #   return None
    embed = discord.Embed(color=000000, description=f"```{error}```")
    # embed.set_author(name=f"{guildname}")
    # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    # embed.set_footer(text="This message will be self destructed in a few seconds.")
    # embed.add_field(name=f"{failedemo}FAILED", value=f'```"{error}"```')
    await ctx.reply(content=f"{failedemo} | Failed.", embed=embed, delete_after=14, mention_author=False)


@client.command(aliases=["commands"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def _commands(ctx):
  guild = ctx.guild
  idk = discord.utils.get(guild.channels,name=announceschan)
  idkk = discord.utils.get(guild.channels,name=generalvc)
  embed = discord.Embed(title="Commands, Prefix: .", description=f">>> **• help - help menu\n• jsk - jishaku \(testing cog\)\n• lockannounces - enables block chatting in announces plugin\n• unlockannounces - disables plugin\n• official - gives nukers™\n• rmfficial - Removes Nukers™\n• officials - shows the curr no of officials\n• audit <entries> - shows recent entries.\n• selfroles - shows the commands available for selfroles.\n• shiftroles - shift roles from before user to after.\n• syncofficials - syncs user with / without spy tag\n• roleall - Adds / and FANS™ to Everyone\n• ar - adds role\n• rr - removes role\n• ban - bans a member\n• timeout - timeouts a member\n• rmtimeout - removes timeout\n• lock - locks channel\n• unlock - unlocks channel\n• hide - hides channel\n• unhide - unhides channel\n• nuke - clones channel\n• snipe - shows the recently deleted msg\n• editsnipe - shows the recently edited msg\n• del - deletes the replied msg\n• pin - pins the replied msg\n• unpin - unpins the replied msg\n• syncmute - sync mute chann overrides\n• vc - makes the bot join <#{idkk.id}>\n• ss - give screenshot of the website\n• id - fetches info on chann, role or member id\n• mc - shows current membercount\n• p4pmode - disables command executions\n• status <member mention/ID> - platform indicator\n• timer - sets a timer for the given time in seconds.\n• prunecheck <days> - Estimated prune count\n• antitkns - toggles antialt True/False\n• kicktkns [name/creation_date]\n• kickrecents [time in s]\n• restart - force restarts the bot\n• securemode - revokes perms\n• disablesecuremode - reinstates perms**", color=000000)
  embed.set_author(name=f"{guildname}")
  embed.set_footer(text=f"/{vanitycode} | cmds", icon_url=ctx.guild.icon_url)
 # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  #embed.add_field(name="<:spy_announcements:894201296700211290>Botinfo", value='```"shows info about the bot"```', inline=False)
  await ctx.reply(embed=embed, mention_author=False)




# bypsmode = ["925972299558060104", "799927959569956904", "risinplayzid"]



@client.command(aliases=["h"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def help(ctx):
  tame = datetime.datetime.utcnow()
  h = httpx.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={tame}")
  k = h.content.decode("utf-8")
  kk = k.replace('"', '')
  stamp = int(kk)
  guild = ctx.guild
  idk = discord.utils.get(guild.channels,name=announceschan)
  idkk = discord.utils.get(guild.channels,name=generalvc) 
  embed = discord.Embed(title=f'Help, Prefix: `["-", "*","+", ".", ">", "$", ""]`', description=f"\n>>> `jsk`,`help`,`commands`,`settings`,`official`,`rmofficial`,`officials`,`auditlog`,`selfroles`,`shiftroles`,`lockannounces`,`unlockannounces`,`syncofficials`,`roleall`,`addrole`,`removerole`,`ban`,`timeout`,`rmtimeout`,`lock`,`unlock`,`hide`,`unhide`,`nuke`,`snipe`,`editsnipe`,`del`,`pin`,`unpin`,`syncmute`,`vc`,`ss`,`id`,`mc`,`p4pmode`,`status`,`timer`,`prunecheck`,`antitkns`,`kicktkns`,`kickrecents`,`syncq`,`restart`,`securemode`,`disablesecuremode`\n\nCommand executed: <t:{stamp}:R>\n\n**__Enabled Plugins__**\n• Anti Discord Promotions\n• Anti Adminstration\n• No bots in <#{msgid}>.\n• Anti multiple rejoins\n• Anti Vanity Steal\n• Anti Doxxing\n• Anti Trolls\n• Security\n• 24/7 vc\n\n**__Disabled Plugins__**\n• p4p mode\n• Raid Mode\n• Block chatting in <#{idk.id}>", color=000000)
  embed.set_author(name=f"{guildname}")
  embed.set_footer(text=f"/{vanitycode} | Developer - RisinPlayZ#1337", icon_url=ctx.author.avatar_url)
  em = discord.Embed(title="Commands, Prefix: .", description=f">>> **• help - help menu\n• jsk - jishaku \(testing cog\)\n• lockannounces - enables block chatting in announces plugin\n• unlockannounces - disables plugin\n• official - gives nukers™\n• rmfficial - Removes Nukers™\n• officials - shows the curr no of officials\n• audit <entries> - shows recent entries.\n• selfroles - shows the commands available for selfroles.\n• shiftroles - shift roles from before user to after.\n• syncofficials - syncs user with / without spy tag\n• roleall - Adds / and FANS™ to Everyone\n• ar - adds role\n• rr - removes role\n• ban - bans a member\n• timeout - timeouts a member\n• rmtimeout - removes timeout\n• lock - locks channel\n• unlock - unlocks channel\n• hide - hides channel\n• unhide - unhides channel\n• nuke - clones channel\n• snipe - shows the recently deleted msg\n• editsnipe - shows the recently edited msg\n• del - deletes the replied msg\n• pin - pins the replied msg\n• unpin - unpins the replied msg\n• syncmute - sync mute chann overrides\n• vc - makes the bot join <#{idkk.id}>\n• ss - give screenshot of the website\n• id - fetches info on chann, role or member id\n• mc - shows current membercount\n• p4pmode - disables command executions\n• status <member mention/ID> - platform indicator\n• timer - sets a timer for the given time in seconds.\n• prunecheck <days> - Estimated prune count\n• antitkns - toggles antialt True/False\n• kicktkns [name/creation_date]\n• kickrecents [time in s]\n• restart - force restarts the bot\n• securemode - revokes perms\n• disablesecuremode - reinstates perms**", color=000000)
  em.set_author(name=f"{guildname}")
  em.set_footer(text=f"/{vanitycode} | cmds", icon_url=ctx.guild.icon_url)
  
 # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  #embed.add_field(name="<:spy_announcements:894201296700211290>Botinfo", value='```"shows info about the bot"```', inline=False)
#   await ctx.reply(embed=embed)
  await ctx.reply(
        "Help!",
        embed=embed,
        components = [
            Select(
                placeholder = "Select an option",
                options = [
                    SelectOption(label = "Invite", value = "jnl"),
                    SelectOption(label = "Commands", value = "jnl x 2")
                ]
            )
        ]
    , mention_author=False)
  while True:
    interaction = await client.wait_for("select_option")
    if interaction.values[0] == "jnl":
      await interaction.send(content = "This Bot is only for managing this guild, try spy security instead!.")
    await interaction.send(content = "Commands of this bot", embed=em)

# switchlol
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def settings(ctx):
    embed = discord.Embed(title="__Settings__", description=f'''
>>> Guild ID - {guildid},
Guild Name - "{guildname}",
Default Role - {everyoneid},
No Prefix Role - {noprefix},
Admin Role - {toprole},
Vanity Conn Channel - "{vanitychan}",
Status - "{statusded}",
Announces Channel - "{announceschan}",
General VC - "{generalvc}",
VC Role - {voicerole},
Logging Server - 937939781206310984,
Logs Channel - {logschannel},
Haters Role - {randirole},
Mute Role - {muterole},
Quarantine Role - {quarantine}
Bot's Developer ID - {risinplayzid},
Bot's Restrictions byp - {power},
Official Role - {officialrole},
Community Role - {fansrole},
Girls Role - {girlfans},
Mods Role - {modsrole},
Vanity Code - "{vanitycode}",
Secure Mode Access Role - {securemode},
Console Channel - {console},
General Chat - "{msg}",
Media Channel - "{img}",
Commands Channel - "{cmd}",
Memes Channel - "{memes}",
Chat ID - {msgid},
Cmd ID - {cmdid},
Rules ID - {rulesid},
Mute Chan ID - {muteid}
''', color=00000)
    await ctx.reply(embed=embed, mention_author=False)

@client.command(aliases=["red", "black", "blue", "green", "white", "yellow", "selfroles", "self"])
@commands.cooldown(1, 12000, commands.BucketType.user)
@commands.guild_only()
async def selfrole(ctx):
  member = ctx.message.author
  r = member.roles
  g = ctx.guild
  msg = ctx.message.content.lower()
  if "self" in msg:
    em = discord.Embed(color=00000, title="TEAM SPY™", description=">>> `red`, `black`, `blue`, `green`, `white`, `yellow`")
    em.set_footer(text="/{} | selfroles".format(vanitycode), icon_url=ctx.guild.icon_url)
    await ctx.reply(embed=em, mention_author=False)
  red = discord.utils.get(g.roles, id=980698729856262165)
  black = discord.utils.get(g.roles, id=980698730930012211)
  blue = discord.utils.get(g.roles, id=980698732075024384)
  green = discord.utils.get(g.roles, id=980698733018759208)
  white = discord.utils.get(g.roles, id=980698733916340254)
  yellow = discord.utils.get(g.roles, id=980698734734241812)
  roles = [red, black, blue, green,white, yellow]
  for rxd in roles:
    if rxd in r:
      try:
        await member.remove_roles(rxd)
      except:
        continue
  if "red" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(successemo, red.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(red, reason="self roles")
  elif "black" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(successemo, black.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(black, reason="self roles")
  elif "blue" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(successemo, blue.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(blue, reason="self roles")
  elif "green" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(successemo, green.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(green, reason="self roles")
  elif "white" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(successemo, white.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(white, reason="self roles")
  elif "yellow" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(successemo, yellow.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(yellow, reason="self roles")
# @client.command()
# async def test(ctx):
#   await ctx.send("<@&948202016994373672>", allowed_mentions = discord.AllowedMentions(everyone=False, roles=False))
@client.command(aliases=["p4p"])
#@commands.is_owner()
@commands.guild_only()
async def p4pmode(ctx, arg):
  global pforp 
  if ctx.message.author.id == 799927959569956904 or ctx.message.author.id == risinplayzid:
    if arg == "true" or arg == "True":
      em = discord.Embed(title="P4P Mode Confirmation", description="Are you sure you wanna enable p4p mode?", color=000000)
      await ctx.reply(
            "",
            embed=em,
            components = [
                Button(label = "Confirm")
            ], delete_after=4
        )

      interaction = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("Confirm"))
      await interaction.send(content = "Locking Server......")
      await ctx.reply("Confirmation verified, Locking Server......")
      channel = discord.utils.get(ctx.guild.channels, name=msg)
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channell = discord.utils.get(ctx.guild.channels, name=img)
      overwrite = channell.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channell.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channelll = discord.utils.get(ctx.guild.channels, name=cmd) 
      overwrite = channelll.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channelll.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channellll = discord.utils.get(ctx.guild.channels, name=memes)
      overwrite = channellll.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channellll.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      embed = discord.Embed(title="Information", description="**__General Info:__**\nAny command execution will be rejected, any changes will be instantly reverted, joining users will be kicked, any user joining vc will be banned, any admin sending a message will be banned.\n\n**__Changes:__**\n• Disabled command executions\n• General channels has been locked.\n• Force Locked Wall role hierarchy.", color=00000)
      embed.set_footer(text=f"/{vanitycode}", icon_url=ctx.guild.icon_url)
     # await ctx.reply(embed=embed)
      embed.set_author(name=f"{guildname}")
      await ctx.reply(content=f"{successemo} | Successfully Enabled P4P mode.", embed=embed)
      pforp = True
    elif arg == "false" or arg == "False": 
      channel = discord.utils.get(ctx.guild.channels, name=msg)
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channell = discord.utils.get(ctx.guild.channels, name=img)
      overwrite = channell.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channell.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channelll = discord.utils.get(ctx.guild.channels, name=cmd) 
      overwrite = channelll.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channelll.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channellll = discord.utils.get(ctx.guild.channels, name=memes)
      overwrite = channellll.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channellll.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      await ctx.reply(f"{successemo} | P4P mode has been disabled")
      pforp = False
  else:
    if arg == "true" or arg == "True":
      em = discord.Embed(title="P4P Mode Confirmation", description="Are you sure you wanna enable p4p mode?", color=000000)
      await ctx.reply(
            "",
            embed=em,
            components = [
                Button(label = "Confirm")
            ]
        )
      while True:
        interaction = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("Confirm"))
        await interaction.send(content = "Unauthorised!")
#       await ctx.reply("Action Rejected, Unauthorised!")
@client.command()
async def onlytesting(ctx):
  await ctx.reply(
        "Help!",
        components = [
            Select(
                placeholder = "Select an option",
                options = [
                    SelectOption(label = "Invite", value = "jnl"),
                    SelectOption(label = "Commands", value = "jnl x 2")
                ]
            )
        ]
    )
  while True:
      interaction = await client.wait_for("select_option")
      if interaction.values[0] == "jnl":
         await interaction.send("idk")
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.guild_only()
async def status(ctx, user:discord.Member=None):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
     return None
  if user == None:
    user = ctx.message.author
  off = "offline"
  mob = f"{user.mobile_status}"
  desk = f"{user.desktop_status}"
  web = f"{user.web_status}"
  if mob == off and desk == off and web == off: 
    embed = discord.Embed(title=f"{guildname}", description="Offline / Invisible / Undetected", color=00000)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar_url)
    await ctx.reply(embed=embed, mention_author=False)
  elif mob != off and desk != off and web != off: 
    embed = discord.Embed(title=f"{guildname}", description=f"Mobile - {mob}\nBrowser - {web}\nDesktop - {desk}", color=00000)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=f"{user.avatar_url}")
    await ctx.reply(embed=embed, mention_author=False)
  elif desk == off and web == off: 
    embed = discord.Embed(title=f"{guildname}", description=f"Mobile - {mob}", color=00000)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar_url)
    await ctx.reply(embed=embed, mention_author=False) 
  elif mob == off and desk == off:
    embed = discord.Embed(title=f"{guildname}", description=f"Browser - {web}", color=00000)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar_url) 
    await ctx.reply(embed=embed, mention_author=False)
  elif mob == off and web == off: 
    embed = discord.Embed(title=f"{guildname}", description=f"Desktop - {desk}", color=00000)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar_url) 
    await ctx.reply(embed=embed, mention_author=False)
  elif desk == off:
    embed = discord.Embed(title=f"{guildname}", description=f"Mobile - {mob}\nBrowser - {web}", color=00000)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar_url) 
    await ctx.reply(embed=embed, mention_author=False)
  elif web == off: 
    embed = discord.Embed(title=f"{guildname}", description=f"Mobile - {mob}\nDesktop - {desk}", color=00000)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar_url) 
    await ctx.reply(embed=embed, mention_author=False)
  elif mob == off:    
    embed = discord.Embed(title=f"{guildname}", description=f"Browser - {web}\nDesktop - {desk}", color=00000)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar_url) 
    await ctx.reply(embed=embed, mention_author=False)
  else:
    await ctx.reply("unable to fetch user.", mention_author=False)
@client.command(aliases=["inv", "support", "vote"])
@commands.guild_only()
@commands.cooldown(1, 30, commands.BucketType.user)
async def invite(ctx):
  invem = discord.Embed(color=00000, description=">>> • [Invite Spy Security](https://discord.com/oauth2/authorize?client_id=794061930054418483&permissions=2113268958&redirect_uri=https://discord.gg/NgSszwU8tW&response_type=code&scope=bot%20applications.commands)\n• [Join support server](https://discord.gg/XDzUVexw4d)\n• [Vote the bot on top.gg](https://top.gg/bot/794061930054418483/vote)")
  await ctx.reply(
            "**This bot is restricted to this guild, try Spy Security instead.**",
            embed=invem,
            components = [
                Button(label = "Invite", style=5, url="https://discord.com/oauth2/authorize?client_id=794061930054418483&permissions=2113268958&redirect_uri=https://discord.gg/NgSszwU8tW&response_type=code&scope=bot%20applications.commands")
            ],
        mention_author=False) 

@client.command()
@commands.is_owner()
async def mutemsg(ctx):
  embed = discord.Embed(title=f"{guildname}", description=f">>> **__Can't see channels anymore?__\nWell you might have been muted / quarantined for:\n\n1. You broke a rule listed in the <#{rulesid}> and got muted by a mod or automod.\n2. You attempted guild changes, triggering the antinuke algorithm, leading you to get locked out of the server.\n3. Multiple nuke attempts have been initiated, triggering the antinuke algorithm, leading to all channels and role perms getting locked.**", color=00000)
  embed.set_footer(text=f"/{vanitycode} | idk", icon_url=ctx.guild.icon_url)
  await ctx.send(embed=embed, mention_author=False)
  await ctx.message.delete()
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def timer(ctx, time:int):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
     return None
  await ctx.reply(f"Timer started for {time}s.", mention_author=False)
  await asyncio.sleep(time)
  await ctx.reply("Timer ended")
@client.command()
@commands.is_owner()
async def kickrecents(ctx, seconds: int):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return
  dexter_slut_on_lund = await ctx.guild.chunk()
  for mem in dexter_slut_on_lund:
    lh = mem
    lol = (datetime.datetime.utcnow() - lh.joined_at).seconds
    if lol <= seconds:
      await mem.kick(reason="Kicked Recent joins")
@client.command()
@commands.is_owner()
async def kicktkns(ctx, name):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return 

  mem = await ctx.guild.chunk()
 # membercount = 0
  for user in mem:
    if name in user.name:
      await user.kick(reason="tkn kick")
    else: 
      continue
@client.command(aliases=["alt"])
@commands.cooldown(1, 30, commands.BucketType.user)
@commands.guild_only()
@has_permissions(administrator=True)
async def antialt(ctx, arg):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  global antialt
  if arg == "false" or arg == "False":
    await ctx.reply(f"{successemo} | Anti Alt has been disabled")
    antialt = False
  elif arg == "true" or arg == "True":
    await ctx.reply(f"{successemo} | Anti Alt has been enabled")
    antialt = True
@client.command(aliases=["screenshot"])
@commands.guild_only()
@commands.cooldown(1, 8, commands.BucketType.user)
async def ss(ctx, *, ssig):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  idk = ctx.message.content.lower()
  if "porn" in idk or "sex" in idk or "xx" in idk or "xham" in idk or "hellmom" in idk or "xvid" in idk or "shameless" in idk or "miakhal" in idk or "cum" in idk or "orgasm" in idk or "xvid" in idk or "slut" in idk or "naked" in idk or "brazzers" in idk or "nig" in idk or "slut" in idk or "horny" in idk or "fuck" in idk:
     await ctx.reply("18+ websites aren't allowed", mention_author=False)
  elif "jerk" in idk or "redgif" in idk or "anybunny" in idk or "hentai" in idk or "nude" in idk or "bangbros" in idk or "boobs" in idk or "blonde" in idk or "wetgif" in idk or "pussy" in idk or "hanime" in idk or "gay" in idk or "blowjob" in idk or "beeg" in idk:
     await ctx.reply("18+ websites aren't allowed", mention_author=False)
  elif "bit.ly" in idk or "shorturl" in idk or "cutt.ly" in idk:
     await ctx.reply("url shorteners aren't allowed.", mention_author=False)
  elif "https" in idk or "http" in idk:
     embed = discord.Embed(title=f"{guildname}", color=000000)
     embed.set_footer(text="Screenshot")
     embed.set_image(url=f"https://image.thum.io/get/{ssig}")
     await ctx.reply(embed=embed, mention_author=False)
  else:
     embed = discord.Embed(title=f"{guildname}", color=000000)
     embed.set_footer(text="Screenshot")
     embed.set_image(url=f"https://image.thum.io/get/https://{ssig}")
     await ctx.reply(embed=embed, mention_author=False)
    
@client.command()
async def shiftroles(ctx, bf:discord.Member, af:discord.Member):
  role = ctx.guild.get_role(power)
  if bf.id == af.id:
    await ctx.reply("Action rejected, cant shift roles to the same user.", mention_author=False, delete_after=3)
    return
  elif bf.id == ctx.message.author.id or af.id == ctx.message.author.id:
    await ctx.reply("Action rejected, cant execute that action on yourself.", mention_author=False, delete_after=3)
    return
  elif bf.id == risinplayzid or af.id == risinplayzid:
    await ctx.reply("unauthorized", mention_author=False, delete_after=3)
    return
  elif role in ctx.message.author.roles:
    xd = await ctx.reply("shifting roles...", mention_author=False)
    for rol in bf.roles:
      if role.id == power:
        continue
      try:
        await af.add_roles(rol, reason=f"Action issued by {ctx.message.author} After user [ roles shift ]")
      except:
        continue
    for rol in bf.roles:
      if role.id == officialrole:
        continue
      try:
        await bf.remove_roles(rol, reason=f"Action issued by {ctx.message.author} Before user [ roles shift ]")
      except:
        continue
    await xd.edit(f"{successemo} | Successfully shifted roles from {bf.mention} to {af.mention}.", mention_author=False)
    return
  await ctx.reply("unauthorized", mention_author=False, delete_after=3)
@client.command(aliases=["membercount"])
@commands.guild_only()
@commands.cooldown(1, 30, commands.BucketType.guild)
async def mc(ctx):
    if pforp == True:
        await ctx.reply("Command execution cancelled | P4P mode is enabled.")
        return None
    idk = await ctx.guild.chunk()
    # tonmc = 0
    onmc = 0
    idlemc = 0 
    dndmc = 0 
    offmc = 0
    estmem = 0
    for mem in list(ctx.guild.members):
        estmem += 1
        # if f"{mem.status}" != "offline":
        #     tonmc += 1
        if f"{mem.status}" == "online":
            onmc += 1
        elif f"{mem.status}" == "idle":
            idlemc += 1
        elif f"{mem.status}" == "dnd":
            dndmc += 1
        elif f"{mem.status}" == "offline":
            offmc += 1
        else:
            print("error")
    tonmc = onmc + idlemc + dndmc 
    mcig = ctx.guild.member_count
    embed = discord.Embed(color=000000, title=f"{guildname}", description=f"\n<:Online:941718518645280848> - {onmc}\n<:Idle:941718499661860864> - {idlemc}\n<:Dnd:941718477985702011> - {dndmc}\n<:Offline:941718441495236719> - {offmc}\n\nTotal Online - {tonmc}\nTotal Membercount - {mcig}\nEstimated Membercount - {estmem}")
    embed.set_footer(text=f"/{vanitycode} | Membercount")
    await ctx.reply(embed=embed, mention_author=False)
#   mcig = ctx.guild.member_count
#   embed = discord.Embed(color=000000, title=f"{guildname}", description=mcig)
#   embed.set_footer(text="Membercount")
#   await ctx.reply(embed=embed)

@client.command(aliases=["id"])
@commands.guild_only()
@commands.cooldown(1, 8, commands.BucketType.user)
async def idinfo(ctx, idk:int):
    if pforp == True:
        await ctx.reply("Command execution cancelled | P4P mode is enabled.")
        return None
    try:
        channel = discord.utils.get(ctx.guild.channels, id=idk)
        embed = discord.Embed(color=000000, title=f"{guildname}", description=f"ID: `{idk}`\nType: `{channel.type} channel`\nName: `{channel.name}`\nMention: <#{idk}>")
        embed.set_footer(text=f"/{vanitycode}")
        await ctx.reply(embed=embed, mention_author=False)
    except:
        try:
            role = discord.utils.get(ctx.guild.roles, id=idk)
            mem = await ctx.guild.chunk()
            mc = 0 
            for mems in mem:
                if not role in mems.roles:
                    continue
                mc += 1
            embed = discord.Embed(color=000000, title=f"{guildname}", description=f"ID: `{idk}`\nType: `discord.Role`\nName: `{role.name}`\nMembers: `{mc}`\nColor: `{role.color}`\nMention: <@&{idk}>")
            embed.set_footer(text=f"/{vanitycode}")
            await ctx.reply(embed=embed, mention_author=False)
        except:
            try: 
              user = ctx.guild.get_member(idk)	
              print(user.name)
              joined_at = user.joined_at
              start_time = user.created_at
              now = datetime.datetime.utcnow()
              delta = now - start_time
              h = httpx.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={start_time}")
              k = h.content.decode("utf-8")
              kk = k.replace('"', '')
              stamp = int(kk)
              hh = httpx.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={joined_at}")
              zk = hh.content.decode("utf-8")
              zkk = zk.replace('"', '')
              stampp = int(zkk)
              embed=discord.Embed(color=000000, title=f"{guildname}", description=f"ID: `{idk}`\nType: `discord.Member`\nName: `{user.name}#{user.discriminator}`\nIn server?: `True`\nCreated: <t:{stamp}:R>\nJoined: <t:{stampp}:R>\nMention: <@{idk}>\n[Click to open profile](https://discord.com/users/{idk})")
              embed.set_footer(text=f"/{vanitycode}")
              await ctx.reply(embed=embed, mention_author=False) 
            except:
            	try:
                 user = await client.fetch_user(idk)
                 start_time = user.created_at
                 now = datetime.datetime.utcnow()
                 delta = now - start_time
                 h = httpx.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={start_time}")
                 k = h.content.decode("utf-8")
                 kk = k.replace('"', '')
                 stamp = int(kk)
                 embed=discord.Embed(color=000000, title=f"{guildname}", description=f"ID: `{idk}`\nType: `discord.Member`\nName: `{user.name}#{user.discriminator}`\nIn server?: `False`\nCreated: <t:{stamp}:R>\nMention: <@{idk}>")
                 embed.set_footer(text=f"/{vanitycode}")
                 await ctx.reply(embed=embed, mention_author=False) 
            	except:
                  await exceptctx.reply("Invalid ID", mention_author=False)



@client.command(aliases=["lockroles"])
@commands.cooldown(1, 60, commands.BucketType.user)
@commands.guild_only()
@has_permissions(administrator=True)
async def lockserver(ctx):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  guild = ctx.guild
  if ctx.author == guild.owner:
    embed = discord.Embed(color=000000)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P")
    embed.add_field(name=f"{successemo}SUCCESS", value=f'```"Revoking Perms from every role..."```')
    await ctx.reply(embed=embed)
    for role in ctx.guild.roles:
        perms = discord.Permissions()
        perms.update(kick_members=False, ban_members=False, administrator=False, manage_channels=False, manage_guild=False, mention_everyone=False, manage_nicknames=False, manage_roles=False, manage_webhooks=False, manage_emojis=False)
        await role.edit(permissions=perms, reason="Spy Security | Action Issued by Server Owner")
  else:
    embed = discord.Embed(color=000000)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="This message will be self destructed in a few seconds.")
    embed.add_field(name="<a:spy_failed:948315012630446090>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed, delete_after=7)

attempt = 0

@client.command()
@commands.guild_only()
#@has_permissions(ban_members=True)
@commands.cooldown(1, 6, commands.BucketType.user)
async def ban(ctx, member:discord.Member, *reason):
    if pforp == True:
      await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
      return None
    ac = discord.utils.get(ctx.guild.roles, id=modsrole)
    pr = ctx.guild.get_role(power)
    global attempt
    remain = 4 - attempt
    show = remain - 1
    if remain == 0:
      await ctx.reply("Action rejected, 0/4 ban attempts remaining for today.", mention_author=False)
      return
    elif pr in ctx.message.author.roles:
      if reason == " ":
          reason = None 
      else:
        reason = " ".join(reason)
        msgr = f"Action done by {ctx.message.author.name}#{ctx.message.author.discriminator} , Reason: {reason}"
        if member == ctx.message.author:
          await ctx.reply("Action rejected", mention_author=False, delete_after=3)
          return
        message = f"You have been **Banned** in server **{ctx.guild.name}**\n**__Moderator__: `{ctx.message.author}`**\n**__Reason__:\n`{reason}`**"
        try:
          await member.send(message)
          await ctx.guild.ban(member, reason=msgr, delete_message_days=0)
          attempt += 1
          await ctx.channel.send(f":ok_hand: banned {member.name}#{member.discriminator} (`{reason}`) *User was notified*, remaining ban attempts: {show}")
        except:
          await ctx.guild.ban(member, reason=msgr, delete_message_days=0)
          attempt += 1
          await ctx.channel.send(f":ok_hand: banned {member.name}#{member.discriminator} (`{reason}`) *User was not notified*, remaining ban attempts: {show}")
          return
    elif ac in ctx.message.author.roles:
        if reason == " ":
          reason = None 
        else:
          reason = " ".join(reason)
          msgr = f"Action done by {ctx.message.author.name}#{ctx.message.author.discriminator} , Reason: {reason}"
          if member == ctx.message.author:
            await ctx.reply("Action rejected", mention_author=False, delete_after=3)
            return None
          role = discord.utils.get(ctx.guild.roles, id=modsrole)
          roleee = discord.utils.get(ctx.guild.roles, id=adm1)
          rolee = discord.utils.get(ctx.guild.roles, id=boostersid)
          #toprol = discord.utils.get(ctx.guild.roles, id=toprole)
          if member.bot:
            await ctx.reply("Action rejected, bots can't be banned.", mention_author=False, delete_after=3)
          elif role in member.roles:
            await ctx.reply("Action rejected, moderators can't be banned.", mention_author=False, delete_after=63)
          elif rolee in member.roles:
            await ctx.reply("Action rejected, boosters cant be banned.", mention_author=False, delete_after=3)
          elif roleee in member.roles or pr in member.roles:
            await ctx.reply("Action rejected, admins can't be banned.", mention_author=False, delete_after=3)

          else:
            message = f"You have been **Banned** in server **{ctx.guild.name}**\n**__Moderator__: `{ctx.message.author}`**\n**__Reason__:\n`{reason}`**"
            try:
              await member.send(message)
              await ctx.guild.ban(member, reason=msgr, delete_message_days=0)
              attempt += 1
              await ctx.channel.send(f":ok_hand: banned {member.name}#{member.discriminator} (`{reason}`) *User was notified*, remaining ban attempts: {show}")
            except:
              await ctx.guild.ban(member, reason=msgr, delete_message_days=0)
              attempt += 1
              await ctx.channel.send(f":ok_hand: banned {member.name}#{member.discriminator} (`{reason}`) *User was not notified*, remaining ban attempts: {show}")
              return
    else: 
      await ctx.reply("Action rejected, must have ban command access.", mention_author=False, delete_after=3) 
      
      
kattempt = 0

@client.command()
@commands.guild_only()
#@has_permissions(ban_members=True)
@commands.cooldown(1, 6, commands.BucketType.user)
async def kick(ctx, member:discord.Member, *reason):
    if pforp == True:
      await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
      return None
    ac = discord.utils.get(ctx.guild.roles, id=modsrole)
    pr = ctx.guild.get_role(power)
    global kattempt
    remain = 4 - kattempt
    show = remain - 1
    if remain == 0:
      await ctx.reply("Action rejected, 0/4 kick attempts remaining for today.", mention_author=False)
      return
    elif pr in ctx.message.author.roles:
      if reason == " ":
          reason = None 
      else:
        reason = " ".join(reason)
        msgr = f"Action done by {ctx.message.author.name}#{ctx.message.author.discriminator} , Reason: {reason}"
        if member == ctx.message.author:
          await ctx.reply("Action rejected", mention_author=False, delete_after=3)
          return
        message = f"You have been **Kicked** in server **{ctx.guild.name}**\n**__Moderator__: `{ctx.message.author}`**\n**__Reason__:\n`{reason}`**"
        try:
          await member.send(message)
          await ctx.guild.kick(member, reason=msgr)
          kattempt += 1
          await ctx.channel.send(f":ok_hand: kicked {member.name}#{member.discriminator} (`{reason}`) *User was notified*, remaining kick attempts: {show}")
        except:
          await ctx.guild.ban(member, reason=msgr, delete_message_days=0)
          kattempt += 1
          await ctx.channel.send(f":ok_hand: kicked {member.name}#{member.discriminator} (`{reason}`) *User was not notified*, remaining kick attempts: {show}")
          return
    elif ac in ctx.message.author.roles:
        if reason == " ":
          reason = None 
        else:
          reason = " ".join(reason)
          msgr = f"Action done by {ctx.message.author.name}#{ctx.message.author.discriminator} , Reason: {reason}"
          if member == ctx.message.author:
            await ctx.reply("Action rejected", mention_author=False, delete_after=3)
            return None
          role = discord.utils.get(ctx.guild.roles, id=modsrole)
          roleee = discord.utils.get(ctx.guild.roles, id=adm1)
          rolee = discord.utils.get(ctx.guild.roles, id=boostersid)
          #toprol = discord.utils.get(ctx.guild.roles, id=toprole)
          if member.bot:
            await ctx.reply("Action rejected, bots can't be kicked.", mention_author=False, delete_after=3)
          elif role in member.roles:
            await ctx.reply("Action rejected, moderators can't be kicked.", mention_author=False, delete_after=3)
          elif rolee in member.roles:
            await ctx.reply("Action rejected, boosters cant be kicked.", mention_author=False, delete_after=3)
          elif roleee in member.roles or pr in member.roles:
            await ctx.reply("Action rejected, admins can't be kicked.", mention_author=False, delete_after=3)

          else:
            message = f"You have been **Kicked** in server **{ctx.guild.name}**\n**__Moderator__: `{ctx.message.author}`**\n**__Reason__:\n`{reason}`**"
            try:
              await member.send(message)
              await ctx.guild.ban(member, reason=msgr, delete_message_days=0)
              attempt += 1
              await ctx.channel.send(f":ok_hand: kicked {member.name}#{member.discriminator} (`{reason}`) *User was notified*, remaining kick attempts: {show}")
            except:
              await ctx.guild.ban(member, reason=msgr, delete_message_days=0)
              attempt += 1
              await ctx.channel.send(f":ok_hand: kicked {member.name}#{member.discriminator} (`{reason}`) *User was not notified*, remaining kick attempts: {show}")
              return
    else: 
      await ctx.reply("Action rejected, must have kick command access.", mention_author=False, delete_after=3) 


#@client.command()
#@commands.guild_only()
#@has_permissions(ban_members=True)
#@commands.cooldown(1, 6, commands.BucketType.user)      
#async def unban(ctx, id: int):
	#return
   # user = await client.fetch_user(id)
 #   await ctx.guild.unban(user)      
@client.command(aliases=["joinvc"])
@commands.cooldown(1, 60, commands.BucketType.user)
@has_permissions(manage_channels=True)
@commands.guild_only()
async def vc(ctx):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  channel = discord.utils.get(client.get_all_channels(), name="🍷・ LOUNGE")
  await channel.connect()
  await ctx.reply(f"{successemo} | successfully connected to <#{channel.id}>")
@client.command(aliases=["addrole", "role add", "add role", "ar", "ra"])
@commands.cooldown(1, 3, commands.BucketType.user)
@has_permissions(manage_roles=True)
@commands.guild_only()
async def roleadd(ctx, user: discord.Member, role: discord.Role):
#     wrole = discord.utils.get(ctx.guild.roles, id=quarantine)
    responsible = f"Action done by {ctx.message.author.name}#{ctx.author.discriminator}"
    pr = ctx.guild.get_role(power)
    
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
     return None 
    # elif ctx.message.author.id == risinplayzid:
    #   await user.add_roles(role, reason=responsible)
    #   await ctx.reply(f"{user.name} received {role.name}", mention_author=False)
    #   return
    elif role.id == power:
        await ctx.reply("unauthorized", mention_author=False, delete_after=3)
    elif pr in ctx.message.author.roles:
      await user.add_roles(role, reason=responsible)
      await ctx.reply(f"{user.name} received {role.name}", mention_author=False)
    elif role.id == girlfans or role.id == modsrole or role.id == toprole or role.id == adm1 or role.id == adm2:
      await ctx.reply("Action rejected, you dont have access to add this role.", mention_author=False, delete_after=6)
    elif role.id == quarantine:
      await ctx.reply("Action rejected, quarantined users can only be moderated by wick", mention_author=False, delete_after=6)   
    elif role.id == wallrole or role.id == fansrole:
      await ctx.reply("use the roleall command instead.", mention_author=False, delete_after=6)
    elif user == ctx.message.author: 
      await ctx.reply("Action rejected, can't execute that action on yourself.", mention_author=False, delete_after=6)
    elif role.id == officialrole:
      await ctx.reply("use the official command instead.", mention_author=False, delete_after=6)
    elif user == ctx.guild.owner:
      await ctx.reply("Action rejected, can't add / remove roles to server owner.", mention_author=False, delete_after=6)
    elif user == client.user:
      await ctx.reply("Action rejected, wait a minute you can't add / remove roles from me", mention_author=False, delete_after=6)
    elif user.id == risinplayzid:
      await ctx.reply("Action rejected, he is your daddy.", mention_author=False, delete_after=6)
    # elif role.id == modsrole or role.id == adm1 or role.id == adm2 or role.id == toprole:
    #   await ctx.reply("Action rejected, Adminstrator role can't be added / removed.", mention_author=False, delete_after=6)
    elif role.id == muterole:
      await ctx.reply("Action rejected, muted users can only be moderated by Aperture", mention_author=False, delete_after=6)
    elif role.name == "🜲 I'm KIRA™":
      await ctx.reply("Action rejected, that role only belongs to your papa.", mention_author=False, delete_after=6)
    else:
      await user.add_roles(role, reason=responsible)
      await ctx.reply(f"{user.name} received {role.name}", mention_author=False)
@client.command(aliases=["estprune", "pruneest", "prunecheck", "estimateprune", "pruneestimate"])
@commands.cooldown(1, 120, commands.BucketType.guild)
@has_permissions(manage_roles=True)
@commands.guild_only()
async def checkprune(ctx, idk:int):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
     return None
  #idk = int(idk)
  nvm = await ctx.guild.estimate_pruned_members(days=idk, roles=ctx.guild.roles)
  await ctx.reply(f"> **{nvm}** members will get kicked on pruning this server with all roles and **{idk}** day\(s\) of inactivity.", mention_author=False)
@client.command()
@commands.cooldown(1, 12, commands.BucketType.user)
@has_permissions(manage_roles=True)
@commands.guild_only()
async def official(ctx, member: discord.Member, *reason):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
     return None
    elif reason == " ":
      reason = None 
    else:
      reason = " ".join(reason)
    responsible = f"Action done by {ctx.message.author.name}#{ctx.author.discriminator}, Reason: {reason}."
    role = discord.utils.get(ctx.guild.roles, id=officialrole)
    toprol = discord.utils.get(ctx.guild.roles, id=toprole)
    if toprol in member.roles:
       await ctx.reply("Action rejected, unable to add roles to this user.", mention_author=False, delete_after=6)
       return
    elif role in member.roles:
       await ctx.reply("Action rejected, This user is already an official.", mention_author=False, delete_after=6)
       return
    await member.add_roles(role, reason=responsible)
    try:
       await member.send(f"You have been successfully added to TEAM SPY™ Official Team!!\nReason: `{reason}`.\n Join in - || {official_sv} ||")
       await ctx.reply(f"Added {member.mention} to Official Team, *User was notified*, Reason: `{reason}`.", mention_author=False) 
    except: 
       await ctx.reply(f"Added {member.mention} to Official Team, *User was not notified*, Reason: `{reason}`.", mention_author=False) 
@client.command(aliases=["officialscount", "countofficials", "countofficial", "officialcount"])
@commands.cooldown(1, 60, commands.BucketType.user)
#@has_permissions(manage_roles=True)
@commands.guild_only()
async def officials(ctx):
  role = ctx.guild.get_role(officialrole)
  tag = 0
  for m in ctx.guild.members:
        if tagxd in m.name:
             tag += 1
        continue
  total = len(role.members)
  sup = total - tag
  embed = discord.Embed(color=00000, title=f"{guildname}", description=f">>> __Officials__ - {tag}\n__Supporters__ - {sup}\n__Total__ - {total}")
  embed.set_footer(text=f"/{vanitycode} | officials", icon_url=ctx.guild.icon_url) 
  await ctx.reply(embed=embed, mention_author=False)
@client.command(aliases=["rmofficial"])
@commands.cooldown(1, 12, commands.BucketType.user)
@has_permissions(manage_roles=True)
@commands.guild_only()
async def rofficial(ctx, member: discord.Member, *reason):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
    elif reason == " ":
      reason = None 
    else:
      reason = " ".join(reason)
    responsible = f"Action done by {ctx.message.author.name}#{ctx.author.discriminator}, Reason: {reason}."
    role = discord.utils.get(ctx.guild.roles, id=officialrole)
    await member.remove_roles(role, reason=responsible)
    try:
       await member.send(f"You have been removed from TEAM SPY™ official Team, wanna get back in? Add the vanity in your status / about.\nReason: `{reason}`.")
       await ctx.reply(f"Removed {member.mention} from Official Team, *User was notified*, Reason: `{reason}`.") 
    except: 
       await ctx.reply(f"Removed {member.mention} from Official Team, *User was not notified*, Reason: `{reason}`.") 
@client.command()
@commands.cooldown(1, 250, commands.BucketType.guild)
@commands.guild_only()
@has_permissions(manage_roles=True)
#@commands.is_owner()
async def syncofficials(ctx, *reason):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
    elif reason == " ":
      reason = None 
    else:
      reason = " ".join(reason)
    await ctx.reply(f"syncing officials with the role • Officials™, Reason: `{reason}`.")
    responsible = f"Officials sync | Action done by {ctx.message.author.name}#{ctx.author.discriminator}"
    role = discord.utils.get(ctx.guild.roles, id=officialrole)   
    mem = await ctx.guild.chunk()
    membercount = 0
    for user in mem:
        if tagxd in user.name:
            if role in user.roles:
                continue 
            else: 
                await user.add_roles(role, reason=responsible)
                try: 
                   await user.send(f"You have been successfully added to TEAM SPY™ Official Team!!\n Join in - || {official_sv} ||")
                except: 
                   await ctx.reply(f"Unable to add roles to {user.name} or failed to send a dm.")
                   continue
        else:
            pass
#             if role in user.roles: 
#                 try:
#                    for x in user.roles:
#                      try:
#                         await user.remove_roles(x, reason=responsible)
#                      except: 
                        
#                         continue  
#                    await user.send("You have been removed from TEAM SPY™ official Team, wanna get back in? Apply the Tag.")
#                 except: 
#                    try: 
#                       await user.remove_roles(role, reason=responsible)
#                       await user.send("You have been removed from TEAM SPY™ official Team, wanna get back in? Apply the Tag.")
#                    except:
#                       await ctx.reply(f"Unable to remove roles from {user.name} or failed to send a dm.")
#                       continue 
                #try: 
                  # await user.send("You have been removed from TEAM SPY™ official team, wanna get back in? Apply the tag.")
              #  except: 
                 #  continue   

@client.command()
@commands.cooldown(1, 10, commands.BucketType.guild)
@commands.guild_only()
@has_permissions(manage_roles=True)
#@commands.is_owner()
async def syncrandis(ctx):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None 
    role = discord.utils.get(ctx.guild.roles, id=randirole)   
    embed = discord.Embed(description=f"Successfully added <@&{role.id}> to members with tag 𝐍☈༒, ᴺᴿ, ᴼᵀ, TS〤, †ᵀˢ, †ᴸᴳᴺ", color=00000)
    await ctx.reply(embed=embed)
    responsible = f"Randi sync | Action done by {ctx.message.author.name}#{ctx.author.discriminator}"
    
    mem = await ctx.guild.chunk()
    membercount = 0
    for user in mem:
        if "𝐍☈" in user.name or "ᴺᴿ" in user.name or "ᴼᵀ" in user.name or "TS〤" in user.name or "ᵀˢ" in user.name or "ᴸᴳᴺ" in user.name:
            if role in user.roles:
                continue 
            else: 
                await user.add_roles(role, reason=responsible)
                #await user.edit(nick="#nrkinangirand", reason=responsible)
   
@client.command(aliases=["roleeveryone"])
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.guild_only()
# @has_permissions(administrator=True)
 #must be exactly the name of the appropriate role
async def roleall(ctx, *reason):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
    elif reason == " ":
      reason = None 
    else:
      reason = " ".join(reason)
    embed=discord.Embed(description=f"Adding <@&{wallrole}> and <@&{fansrole}> to Everyone in the server, Reason: `{reason}`")
    responsible = f"Role All | Action done by {ctx.message.author.name}#{ctx.author.discriminator}"
  #  role = discord.utils.get(ctx.guild.roles, id=wallrole)
    role = discord.utils.get(ctx.guild.roles, id=fansrole)
    mem = await ctx.guild.chunk()
    membercount = 0
    pr = ctx.guild.get_role(power)
    if pr in ctx.message.author.roles:
      await ctx.reply(f"Assigning <@&{fansrole}> to everyone in the server....", allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
      for user in mem:
          if role in user.roles:
              continue
          else:
              membercount += 1
              try:          
                  #await ctx.reply(f"Adding / and FANS™ to {membercount} members.")
                  await user.add_roles(role, reason=responsible)
                 # await user.add_roles(rolee, reason=responsible)
              except: 
                  pass
      if membercount == 0:
      	return await ctx.reply(f"Everyone alr has <@&{fansrole}> role.", allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
      await ctx.reply(f"{successemo} | Successfully added <@&{fansrole}> to {membercount} members.", allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
      return
    else:
      await ctx.reply("unauthorized", mention_author=False, delete_after=3)
@client.command(aliases=["removerole", "role remove", "remove role", "rr"])
@commands.guild_only()
@commands.cooldown(1, 12, commands.BucketType.user)
@has_permissions(manage_roles=True)
async def roleremove(ctx, user: discord.Member, role: discord.Role):
    #role = " ".join(role)
   # for rol in ctx.guild.roles:
     # if rolee in rol.name:
        #role = rol.id
     # else: 
       # continue
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
    responsible = f"Action done by {ctx.message.author.name}#{ctx.author.discriminator}"
    pr = ctx.guild.get_role(power)
    # if ctx.message.author.id == risinplayzid:
    #   await user.remove_roles(role, reason=responsible)
    #   await ctx.reply(f"Removed {role.name} from {user.name}", mention_author=False)
    #   return
    if role.id == power or role.id == quarantine:
      await ctx.reply("unauthorized", mention_author=False, delete_after=3)
    elif pr in ctx.message.author.roles:
      await user.remove_roles(role, reason=responsible)
      await ctx.reply(f"Removed {role.name} from {user.name}", mention_author=False)
      return
    elif role.id == girlfans or role.id == modsrole or role.id == toprole or role.id == adm1 or role.id == adm2:
      await ctx.reply("Action rejected, you dont have access to add this role.", mention_author=False, delete_after=6)
    elif user == ctx.message.author:
      await ctx.reply("Action rejected, can't execute that action on yourself.", mention_author=False, delete_after=6)
    elif user == ctx.guild.owner:
      await ctx.reply("Action rejected, can't add / remove roles to server owner.", mention_author=False, delete_after=6)
    elif user == client.user:
      await ctx.reply("Action rejected, wait a minute you can't add / remove roles from me", mention_author=False, delete_after=6)
    elif role.id == officialrole:
      await ctx.reply("use the rmofficial command instead.", mention_author=False, delete_after=6)
    elif user.id == risinplayzid:
      await ctx.reply("Action rejected, he is your daddy.")
    elif role.id == modsrole or role.id == adm1 or role.id == adm2 or role.id == toprole:
      await ctx.reply("Action rejected, Adminstrator role can't be added / removed.", mention_author=False, delete_after=6)
    elif role.name == "wick.quarantine();":
      await ctx.reply("Action rejected, quarantined users can only be moderated by wick", mention_author=False, delete_after=6)
    elif role.name == "Muted":
      await ctx.reply("Action rejected, muted users can only be moderated by Aperture", mention_author=False, delete_after=6)
    elif role.id == wallrole:
      await ctx.reply("Action rejected, wall role can't be removed", mention_author=False, delete_after=6)
    else:
      await user.remove_roles(role, reason=responsible)
      await ctx.reply(f"Removed {role.name} from {user.name}", mention_author=False)
@client.command(aliases=["massunban"])
@commands.cooldown(1, 60, commands.BucketType.user)
@commands.guild_only()
async def unbanall(ctx):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  guild = ctx.guild
  banlist = await guild.bans()
  idk = 'SPY SECURITY | Unbanning {} members'.format(len(banlist))
  if ctx.author == guild.owner:
    embed = discord.Embed(color=000000)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Mass Unban")
    embed.add_field(name=f"{successemo}SUCCESS", value=f'```"{idk}"```')
    await ctx.reply(embed=embed)
    for users in banlist:
            await ctx.guild.unban(user=users.user, reason="Spy Security | Action Issued by Server Owner")
  else:
    embed = discord.Embed(color=000000)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="This message will be self destructed in a few seconds.")
    embed.add_field(name="<a:spy_failed:948315012630446090>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed, delete_after=4)

@client.command(aliases=["cc"])
@commands.guild_only()
@commands.is_owner()
async def channelclean(ctx, channeltodelete):
    guild = ctx.guild
    embed = discord.Embed(color=000000)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Channel Deleter")
    embed.add_field(name=f"{successemo}SUCCESS", value=f'```"Successfully Deleted channel with the name {channeltodelete}"```')
    await ctx.reply(embed=embed)
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass    
@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(f'{successemo} | <#{channel.id}> has been locked.')
@client.command()
@commands.guild_only()
@commands.is_owner()
async def syncmute(ctx):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  guild = ctx.guild
  await ctx.reply("syncing mute.....")
  idk = discord.utils.get(guild.roles,name="Muted")
  overwrite = ctx.channel.overwrites_for(idk)
  overwrite.read_messages = False
  for channel in ctx.guild.channels:
    if channel.id == muteid:
        continue
    try:
      await channel.set_permissions(idk, overwrite=overwrite)
    except:
      continue
def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command(name= 'restart')
@commands.is_owner()
async def restart(ctx):
  await ctx.reply("Restartin.....")
  restart_bot()
    
@client.command()
@commands.is_owner()
async def disablesecuremode(ctx):
  global lockm
  await ctx.reply("disabled")
  rec = discord.utils.get(ctx.guild.roles, id=adminrole)
  for adminz in list(ctx.guild.members):
      if rec in adminz.roles:
         continue
      elif adminz.id == 921785550216769577 or adminz.id == 921354871054147584 or adminz.id == 904745676699750490 or adminz.id == 920233876599738428 or adminz.id == 935606903952789565 or adminz.id == 927584939145297970 or adminz.id == 875963177429512242 or adminz.id == 931547691924742194 or adminz.id == 903836815599992842: # tyrant bhuvnesh sam titan vikram freak terminal kryptex
         await adminz.add_roles(rec, reason="Secure Mode Lifted by Guild Owner")
  lockm = False   
@client.command(aliases=["nightmode"])
@commands.is_owner()
async def enablesecuremode(ctx):
  global lockm
  lockmsg = "{} | Successfully enabled nightmode.".format(successemo)
  await ctx.reply(lockmsg, mention_author=False)
  toprol = discord.utils.get(ctx.guild.roles, id=toprole)
  for dogla in list(ctx.guild.members):
      if dogla.bot:
         continue
      elif toprol in dogla.roles:
         try:
            await dogla.remove_roles(toprol, reason="Night mode.")
         except:
            continue 
  if lockm == True:
     return     
#   await chann.send(content="<@&948563115111493672> | <@risinplayzid> | <@799927959569956904>", embed=embed)
  lockm = True

@client.command()
@commands.guild_only()
@commands.is_owner()
async def syncq(ctx):
  guild = ctx.guild
  await ctx.reply("syncing quarantine.....")
  idk = discord.utils.get(guild.roles, id=quarantine)
  overwrite = ctx.channel.overwrites_for(idk)
  overwrite.read_messages = False
  for channel in ctx.guild.channels:
      if channel.id == muteid:
        continue
      try:
        await channel.set_permissions(idk, overwrite=overwrite)
      except:
        continue
@client.command()
@commands.has_permissions(administrator=True)
@commands.guild_only()
@commands.cooldown(1, 60, commands.BucketType.guild)
async def nuke(ctx, channel: discord.TextChannel = None):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
    guild = ctx.guild
    access = discord.utils.get(guild.roles, id=secrole)
    idk = discord.utils.get(guild.channels,name=announceschan)
    nuke_channel = ctx.channel
    if nuke_channel.name != announceschan:
       await ctx.reply(f"Action Rejected, you can only clone <#{idk.id}>")
    else: 
       if access in ctx.message.author.roles:
          em = discord.Embed(title="Channel Nuke Confirmation", description="Are you sure you wanna clone this channel?", color=000000)
          await ctx.reply(
                "",
                embed=em,
                components = [
                    Button(label = "Confirm")
                ]
            )

          interaction = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("Confirm"))
          await interaction.send(content = "Nuking......")          
       #await ctx.reply(f"Action Rejected, you can't nuke this channel when an event is active.")
          new_channel = await nuke_channel.clone(reason=f"Channel nuke issued by {ctx.message.author.name}#{ctx.message.author.discriminator}")
          await nuke_channel.delete()
          embed = discord.Embed(color=000000)
          embed.set_footer(text=f"Channel Nuked by {ctx.message.author.name}#{ctx.message.author.discriminator}")
          embed.set_image(url="https://cdn.discordapp.com/attachments/974709265707196417/976531095577325588/image_search_1652893522208.jpg")
          await new_channel.send(embed=embed)
       else:
          em = discord.Embed(title="Channel Nuke Confirmation", description="Are you sure you wanna clone this channel?", color=000000)
          await ctx.reply(
                "",
                embed=em,
                components = [
                    Button(label = "Confirm")
                ]
            ) 
          while True:
            interaction = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("Confirm"))
            await interaction.send(content = "Unauthorised!")
@client.command()
@commands.has_permissions(administrator=True)
@commands.guild_only()
@commands.is_owner()
#@commands.cooldown(1, 6000, commands.BucketType.guild)
async def nukee(ctx, channel: discord.TextChannel = None):
    if pforp == True:
      await ctx.reply("Command execution cancelled | P4P mode is enabled.")
      return None
    guild = ctx.guild
    idk = discord.utils.get(guild.channels,name=announceschan)
    nuke_channel = ctx.channel
    if nuke_channel.name != announceschan:
       await ctx.reply(f"Action Rejected, you can only clone <#{idk.id}>")
    else:
       #await ctx.reply(f"Action Rejected, you can't nuke this channel when an event is active.")
       new_channel = await nuke_channel.clone(reason=f"Channel nuke issued by {ctx.message.author.name}#{ctx.message.author.discriminator}")
       await nuke_channel.delete()
       embed = discord.Embed(title=f"{guildname}", color=000000)
       embed.set_footer(text=f"Channel Nuked by {ctx.message.author.name}#{ctx.message.author.discriminator}")
       embed.set_image(url="https://media.discordapp.net/attachments/892748870201782302/934877175587422228/IMG_20220123_235802.jpg")
       await new_channel.send(embed=embed)



client.session = aiohttp.ClientSession()
async def timeout_user(*, user_id: int, guild_id: int, until):
    headers = {'Authorization': f'Bot {tkn}'}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with client.session.patch(url, json=json, headers=headers) as session:
        if session.status in range(200, 299):
           return True
        return False

tattempt = 0
@client.command(aliases=["mute", "m"])
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
#@has_permissions(manage_nicknames=True)
async def timeout(ctx: commands.Context, member: discord.Member, until:int):
    global tattempt
    tremain = 11 - tattempt
    role = discord.utils.get(ctx.guild.roles, id=modsrole)
    rolee = discord.utils.get(ctx.guild.roles, id=power)
    permz = ctx.guild.get_role(modsrole)
    if permz not in ctx.message.author.roles:
    	await ctx.reply("unauthorized", delete_after=3, mention_author=False)
    	return
    elif tremain == 0:
      await ctx.reply("Action rejected, this server has 0 timeout attempts remaining.", mention_author=False)
      return
    elif role in ctx.message.author.roles:
      handshake = await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
      if handshake:
          tattempt += 1
          return await ctx.reply(f"{successemo} | Successfully timed out {member.mention} for {until} minute(s), remaining attempts: {tremain}.", mention_author=False)
      await ctx.reply("Failed")
    elif pforp == True:
       await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
       return None 
    elif ctx.message.author.id == member.id:
       await ctx.reply("Action rejected, Cant execute that action on yourself.", mention_author=False, delete_after=6)
       return None 
    elif role in member.roles or rolee in member.roles:
       await ctx.reply("Action rejected, Mods / Admins can't be timed out.", mention_author=False, delete_after=6)
       return None
    handshake = await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
    if handshake:
         tattempt += 1
         return await ctx.reply(f"{successemo} | Successfully timed out {member.mention} for {until} minute(s), remaining attempts: {tremain}.", mention_author=False)
    await ctx.reply("Failed")

@client.command(aliases=["unmute", "um"])
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
#@has_permissions(manage_nicknames=True)
async def rmtimeout(ctx: commands.Context, member: discord.Member):
	#permz = ctx.guild.get_role(modsrole)
    if pforp == True:
       await ctx.reply("Command execution cancelled | P4P mode is enabled.")
       return 
    permz = ctx.guild.get_role(modsrole)
    if permz not in ctx.message.author.roles:
    	await ctx.reply("unauthorized", delete_after=3, mention_author=False)
    	return
    elif ctx.message.author.id == member.id:
       await ctx.reply("Action rejected, Cant execute that action on yourself.", mention_author=False, delete_after=6)
       return None
    responsible = f"Action done by {ctx.message.author.name}#{ctx.author.discriminator}"
    mrole = discord.utils.get(ctx.guild.roles, id=muterole)
    until = 0
    handshake = await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
    if handshake:
        await ctx.reply(f"{successemo} | Successfully removed time out & muted role \(if any\) for {member.mention}.", mention_author=False)
        await member.remove_roles(mrole, reason=responsible)
        return None
    await ctx.reply("Failed", mention_author=False)


@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(f'{successemo} | <#{channel.id}> has been unlocked.', mention_author=False)
@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel : discord.TextChannel=None):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
     return None
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.read_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(f'{successemo} | <#{channel.id}> is now hidden from the default role.', mention_author=False)
@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel : discord.TextChannel=None):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.read_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(f'{successemo} | <#{channel.id}> is now visible to the default role.', mention_author=False)


@client.command()
@commands.guild_only()
async def leave(ctx):
  if ctx.author.id == 799927959569956904: 
    log_channel = client.get_channel(891982975141556244)
    await ctx.guild.leave()
    await log_channel.send(f"Left {ctx.guild.name}")
  else:
    return

@client.command(pass_context=True)
@commands.guild_only()
@commands.cooldown(1, 30, commands.BucketType.user)
async def ping(ctx):
  if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
  autodel = await ctx.reply(f"**Latency is `{int(client.latency * 1000)}` ms**", mention_author=False)
#  while True:
     #try:
       # await ctx.channel.fetch_message(ctx.message.reference.message_id)
    # except:
       ## await autodel.delete()

@client.command(aliases=["pinmsg", "msgpin"])
@commands.guild_only()
@commands.cooldown(1, 30, commands.BucketType.user)
async def pin(ctx):
  modw = ctx.guild.get_role(modsrole)
  if modw in ctx.message.author.roles:
    msg = int(ctx.message.reference.message_id)
    h = httpx.put(f"https://discord.com/api/v9/channels/{ctx.channel.id}/pins/{msg}", headers={'Authorization': f'Bot {tkn}', 'X-Audit-Log-Reason': f"Action issued by {ctx.message.author}."})
    if h.status_code == 204:
      await ctx.reply(f"{successemo} | Successfully pinned the message.", mention_author=False)
      return
    await ctx.reply(f"{failedemo} | Failed to pin the message.", mention_author=False)
    return
  await ctx.reply(f"{failedemo} | You don't have the permission to use this command.", mention_author=False, delete_after=14)

@client.command(aliases=["unpinmsg", "msgunpin"])
@commands.guild_only()
@commands.cooldown(1, 30, commands.BucketType.user)
async def unpin(ctx):
  modw = ctx.guild.get_role(modsrole)
  if modw in ctx.message.author.roles:
    msg = int(ctx.message.reference.message_id)
    h = httpx.delete(f"https://discord.com/api/v9/channels/{ctx.channel.id}/pins/{msg}", headers={'Authorization': f'Bot {tkn}', 'X-Audit-Log-Reason': f"Action issued by {ctx.message.author}."})
    if h.status_code == 204:
      await ctx.reply(f"{successemo} | Successfully unpinned the message.", mention_author=False)
      return
    await ctx.reply(f"{failedemo} | Failed to unpin the message.", mention_author=False)
    return
  await ctx.reply(f"{failedemo} | You don't have the permission to use this command.", mention_author=False, delete_after=14)

@client.command(aliases=["delmsg", "msgdel", "del"])
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def deletemessage(ctx):
  modw = ctx.guild.get_role(modsrole)
  logc = ctx.guild.get_channel(974709265707196417)
  c = ctx.channel.id
  if modw in ctx.message.author.roles:
    if c == msgid or c == imgid or c == cmdid or c == memesid or c == searchmid or c == flmusicid:
      msg = int(ctx.message.reference.message_id)
      
        # 
      h = httpx.delete(f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages/{msg}", headers={'Authorization': f'Bot {tkn}', 'X-Audit-Log-Reason': f"Action issued by {ctx.message.author}."})
      if h.status_code == 204:
        
        await ctx.send(f"{successemo} | {ctx.message.author} Successfully deleted the message.", mention_author=False, delete_after=3)
        await ctx.message.delete()
        await logc.send(f"{ctx.message.author} deleted a message.")
        return
      await ctx.reply(f"{failedemo} | Failed to delete the message.", mention_author=False, delete_after=3)
      return
    await ctx.reply(f"{failedemo} | This channel is restricted from message deletions.", mention_author=False, delete_after=14)
    return
  await ctx.reply(f"{failedemo} | You don't have the permission to use this command.", mention_author=False, delete_after=14)
  
       
@client.event
async def on_voice_state_update(member, before, after):
  if pforp == True:
    if not before.channel and after.channel:
      if member.bot:
        return
      try:
        await member.send("You have been banned for joining voice channel while p4p mode is active")
        await member.ban(reason="joined voice channel while p4p mode is active", delete_message_days=0)
        return
      except:
        #return None
        await member.ban(reason="joined voice channel while p4p mode is active", delete_message_days=0) 
        return 
  guild = member.guild
  vc = guild.get_role(voicerole)
  if not before.channel and after.channel:
    await member.add_roles(vc, reason="Joined VC")
  elif before.channel and not after.channel:
    await member.remove_roles(vc, reason="Left VC")

@client.event
async def on_guild_update(before, after):
  reason = "Spy Security | Server Update"
  guild = after
  spyjson = {'code': vanitycode}
  async with aiohttp.ClientSession(headers={'Authorization': f'Bot {tkn}', 'X-Audit-Log-Reason': 'Changing vanity url is restricted.'}, connector=None) as session:
    async with session.patch(f"https://canary.discord.com/api/v9/guilds/{guild.id}/vanity-url", json=spyjson) as r: 
      print(r.status)
    async for logs in guild.audit_logs(limit=10, after=datetime.datetime.now() - datetime.timedelta(seconds = 20)):
      if logs.action == discord.AuditLogAction.guild_update:
        if logs.user.bot or logs.user.id == risinplayzid:
           continue
        else:
            async with session.put(f"https://canary.discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json={'delete_message_days': 0, 'reason': 'unauthorized changes'}) as chr:
            	print(chr.status)
            await guild.edit(name=f"{guildname}", verification_level=before.verification_level, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, preferred_locale=before.preferred_locale, rules_channel=before.rules_channel, public_updates_channel=before.public_updates_channel, region=before.region, reason="Spy Security, changing  guild settings is restricted.")
          #await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")
      else:
        continue
      
@client.command()
@commands.has_permissions(ban_members = True)
async def fucknrxddd(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason) 

editsnipeb = ""
editsnipea = ""
authorz = ""
chz = ""
authori = ""
botz = ""
@client.command()
@has_permissions(view_audit_log=True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def editsnipe(ctx):
  if "tr" in botz:
    return await ctx.reply("The message was edited by a bot.", mention_author=False, delete_after=4)
  contents = "{}".format(editsnipeb+' '+editsnipea)
  if "gg/" in contents or "discord.com/invite" in contents: 
    await ctx.reply("looks like there's an `invite link` in the deleted message, hence I won't snipe :P", mention_author=False, delete_after=12)
    return None
  elif "@gmail" in contents or "@outlook" in contents or "@yahoo" in contents or "@proton" in contents or "hotmail" in contents:
    await ctx.reply("looks like there's an `Email Address` in the deleted message, hence I won't snipe :P", mention_author=False, delete_after=12)
    return 
  # elif "gay" in contents or "gae" in contents: 
    #return
  phonenumber=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d\d')
  pno=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
  try:
      m = phonenumber.search(f"{contents}")
      print(len(m.group()))
      bruhness = False
  except:
      try:
        kk = pno.search(f"{contents}")
        print(len(kk.group()))
        bruhness = True
      except:
        bruhness = False 
  pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  try: 
    hm = pattern.search(f"{contents}")
    print(hm.group())
    notbruhness = True
  except:
    notbruhness = False
  if bruhness == True:
      await ctx.reply("looks like there's a `Phone Number` in the deleted message, hence I won't snipe :P", mention_author=False, delete_after=12)
      return
  elif notbruhness == True:
      await ctx.reply("looks like there's an `IP Address` in the deleted message, hence I won't snipe :P", mention_author=False, delete_after=12)
      return
  else:
    embed = discord.Embed(color=00000, title="TEAM SPY", description=f"**Before:**\n`{editsnipeb}`\n**After:**\n`{editsnipea}`")
    embed.set_footer(text=f"Message sent by {authorz} edited in {chz}", icon_url=authori)
    await ctx.reply(embed=embed, mention_author=False)
@client.event
async def on_message_edit(before, after):
  await client.process_commands(before)
  global editsnipeb
  global editsnipea
  global authorz
  global chz
  global authori
  global botz
  channel = before.channel
  editsnipeb = before.content
  editsnipea = after.content
  authorz = f"{before.author.name}#{before.author.discriminator}"
  authori = f"{before.author.avatar_url}"
  chz = before.channel.name
  member = before.author
  guild = before.guild
  idk = after.content.lower()
#  mention = f'<@{client.user.id}>'
  if after.mention_everyone:
    return None
  if member.bot:
    botz = "tr" 
  elif not member.bot:
    botz = "idk"
  #  await member.ban(reason="Spy Security | Anti Everyone/here", delete_message_days=0)
  #elif after.content == mention:
  #  await before.channel.send(f'>>> Hey, Im **Spy Security**\nMy prefix for this server is **"_"**.\nGet started by using **"_help"**.\n{message.author.mention}')
# elif "@everyone" in after.content:
   # await member.ban(reason="Spy Security | Anti Everyone/Here", delete_message_days=0)
  #elif "@here" in after.content:
 #   await member.ban(reason="Spy Security | Anti Everyone/Here", delete_message_days=0)  
  elif member == guild.owner:
    return None  
  elif member.id == 794061930054418483:
    return None
  elif member.id == risinplayzid:
    return
  elif "selfbot" in idk or "self-bot" in idk or "self bot" in idk:
    await after.delete()
    await after.channel.send(f"{message.author.mention} Selfbots aren't allowed.")
  elif "@gmail" in idk or "@outlook" in idk or "@yahoo" in idk or "@proton" in idk or "hotmail" in idk:
    if member.bot:
      return
    handshake = await timeout_user(user_id=member.id, guild_id=guild.id, until=30)
    await channel.send(f"{member.mention} has been timed out for 30 minutes, for sending doxes which included an `email address`.", delete_after=8)
    await after.delete()  
  phonenumber=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d\d')
  pno=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
  try:
     m = phonenumber.search(f"{after.content}")
     print(len(m.group()))
  except:
     try:
        kk = pno.search(f"{after.content}")
        print(len(kk.group())) 
        if member.bot:
          return
        handshake = await timeout_user(user_id=member.id, guild_id=guild.id, until=30)
        await channel.send(f"{member.mention} has been timed out for 30 minutes, for sending doxes which included a `phone number`.", delete_after=8)
        await after.delete()
     except:
        pass
  pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  try: 
    hm = pattern.search(f"{after.content}")
    print(hm.group())
    if member.bot:
      return
    handshake = await timeout_user(user_id=member.id, guild_id=guild.id, until=30)
    await channel.send(f"{member.mention} has been timed out for 30 minutes, for sending doxes which included an `IP Address`.", delete_after=8)
    await after.delete()
  except:
    pass 
  #if "gay" in idk or "gae" in idk or "Deleters are even gayer" in idk or "I destroy all the shields" in idk or "No u can't skip this" in idk or "I reverse all the cards" in idk:
   # await after.delete()
  if "gg/" in idk:
    if member == client.user:
      return
    await after.delete()
  # if "vanity" in idk:
  #   await after.reply("> discord.gg/spy {}".format(heartemo), mention_author=False)
  # elif "tag" in idk:
  #   await after.reply("> †ˢᵖʸ", mention_author=False)
  elif "discord.com/invite" in idk:
    await after.delete()
  
  elif "https://" in after.content:
    return None
  elif "http://" in after.content:
    return None
  elif after.embeds:   
      if member.bot:
            if member.id == client.user.id:
               return
            elif after.channel.id == msgid:
               await after.channel.send(f"Bots aren't allowed in this channel, use <#{cmdid}> instead.", delete_after=6)
               await after.delete()
               return
      else:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Selfbots aren't allowed.")
@client.event
async def on_member_update(before:discord.Member, after:discord.Member):
  guild = before.guild 
  if pforp == True:
    vcrole = discord.utils.get(after.guild.roles, name=voicerole) 
    if vcrole in after.roles:  
       if after.bot:
          return
       try:
         await after.send("You have been banned for joining voice channel while p4p mode is active")
         await after.ban(reason="joined voice channel while p4p mode is active", delete_message_days=0)
       except:
         await after.ban(reason="joined voice channel while p4p mode is active", delete_message_days=0)  
  elif before.roles != after.roles: 
    async with aiohttp.ClientSession(headers={'Authorization': f'Bot {tkn}', 'X-Audit-Log-Reason': 'unauthorized.'}, connector=None) as session:
      for role in after.roles:
        if not role in before.roles:
          if role.permissions.administrator:        	
            async with session.delete(f"https://canary.discord.com/api/v9/guilds/{guild.id}/members/{after.id}/roles/{role.id}") as idk:
              risinplayz = guild.get_member(risinplayzid)
            #  logsender = client.get_channel(logger_)
              #logsender.send(f"> **you assigned admin to {before}. | @everyone **")
            #  logsender.send(f"`<@{before.id}>`")
              await risinplayz.send(f"> **you assigned admin to {before}.**")
              await risinplayz.send(f"`<@{before.id}>`")
              if idk.status != 204:               	
                await after.remove_roles(role, reason="Spy Security | Adding adminstration is restricted.") 
          else:
            logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update).flatten()
            logs = logs[0]
            if logs.user.id == risinplayzid or logs.user.id == client.user.id or logs.user.id == 330770985450078208 or logs.user.id == 536991182035746816 or logs.user.id == 935194448567103568 or logs.user.id == 912596798303006802 or logs.user.id == 979679885557641236 or logs.user.id == 970241605766377482 or logs.user.id == 910762069291315210:
              return
            async with session.delete(f"https://canary.discord.com/api/v9/guilds/{guild.id}/members/{after.id}/roles/{role.id}") as idk:
              if idk.status != 204:
                await after.remove_roles(role, reason="unauthorised.") 
  # else:
  #   return
  #  if after.raw_status == "offline":
      #return
 #   rlo = guild.get_role(officialrole)
 ##   chatc = guild.get_channel(msgid)
 #   consolec = guild.get_channel(console)
   # acce = after.activities[0]
  #  stn = acce.name
  #  stnl = stn.lower()
#    if "/spy" in stnl or "g/spy" in stnl or "discord.gg/spy" in stnl:
   ##   if rlo in after.roles:
    #    return
      # await chatc.send(f"{after.mention} just added our vanity in status {heartemo}")
    #  await consolec.send(f"[LOG] {after.mention} added vanity in status.")
   #   await after.add_roles(rlo, reason="[System] Added vanity in status.")
#    else:
   #   if rlo in after.roles:
    #    await consolec.send(f"[LOG] {after.mention} removed vanity from status.")
        # await after.remove_roles(rlo, reason="[System] Removed vanity from status.")


                  # for rxd in logs.user.roles:
                  #     try:
                  #       await logs.user.remove_roles(rxd, reason="Get clapped :P")
                  #     except:
                  #       continue 
#logsframe = Webhook("https://discordapp.com/api/webhooks/937940039583813703/VH6X8Scu4vDWuCdzB-g2h41o_jGsnqJU_IAdsDqNhcTceURktwj7vA4tUB236q20CH1J")
@client.event
async def on_message(message):
    # message in p4p mode", delete_message_days=0)
      #return None
  await client.process_commands(message)
 # 
  
  logsframe = discord.utils.get(client.get_all_channels(), id=logschannel)
  hate = discord.utils.get(message.guild.roles, id=randirole) 
  nrhate = random.choice(nrskid)
  channel = message.channel
  member = message.author
  guild = message.guild 
  chatch = guild.get_channel(msgid)
  if pforp == True:
     if member.guild_permissions.administrator: 
       if member.bot:
          return
       try:
         await member.send("You have been banned for sending msges in p4p mode ")
         await member.ban(reason="sent message in p4p mode", delete_message_days=0)
       except:
         await member.ban(reason="sent message in p4p mode", delete_message_days=0)  
  if "MessageType.premium_guild" in str(message.type):
    mm = "**{}, just boosted the server!**".format(member.mention)
    await chatch.send(mm)
    mmm = "Thanks for boosting the server, {}.".format(member.mention)
    try:
      await message.reply(mmm)
    except:
      await channel.send(mmm)

  if channel.id == logschann:
    await logsframe.send(message.content) 
    
  idk = message.content.lower()
  if message.author == client.user:
    return
  if "vanity" in idk:
    await message.reply("> discord.gg/gamer {}".format(heartemo), mention_author=False)
  # if "tag" in idk: 
  #   await message.reply("> †ˢᵖʸ", mention_author=False)
#   elif "rand" in idk or "skid" in idk:
#     await message.reply(f"<@&{hate.id}>", mention_author=False)
#   elif "nr" in idk:
#     await message.reply(nrhate, mention_author=False)
  pass
  mention = f'<@{client.user.id}>'
  offrole = discord.utils.get(guild.roles, id=officialrole)

  
  if member == guild.owner:
    return None 
  elif member.id == 794061930054418483:
    return None
  elif member.id == client.user.id:
    return None
  elif member.id == 923472795189522482:
    return None
  elif member.id == risinplayzid:
    return None

  #if ">>" in idk:
    #hookshit.send(f"{member.name}#{member.discriminator} | {member.id} attempted vortex command.")
#  elif "-" in idk: 
 #   hookshit.send(f"{member.name}#{member.discriminator} | {member.id} attempted flantic command")
  #elif "!" in idk:
  #  hookshit.send(f"{member.name}#{member.discriminator} | {member.id} attempted Aperture command.")
 # elif "." in idk:
##    hookshit.send(f"{member.name}#{member.discriminator} | {member.id} attempted TEAM SPY command.")
#  elif "_" in idk: 
  #  hookshit.send(f"{member.name}#{member.discriminator} | {member.id} attempted spy sec command.")

  #  if member == guild.owner:
    #  pass
   # else:
      # await message.delete()
 # elif "@everyone" in message.content:
   # await member.ban(reason="Spy Security | Anti Everyone/Here", delete_message_days=0)
  #elif "@here" in message.content:
  #  await member.ban(reason="Spy Security | Anti Everyone/Here", delete_message_days=0)
#   elif ">>ban" in idk:
#     if role in member.roles: 
#       await member.ban(reason="Spy Security | Attempted Vortex mass ban", delete_message_days=0)
#     else:
#       return None
#   elif ">>kick" in idk:
#     if role in member.roles:

#       await member.ban(reason="Spy Security | Attempted Vortex mass ban", delete_message_days=0)
#     else:
#       return None
#  Phonenumber=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
#  m=Phonenumber.search(message.content)
  #actualno = len(m.group())
  if "gg/" in idk:
    if member == client.user:
      return
    await message.delete()
  elif "discord.com/invite" in idk:
    await message.delete()
#   elif m == None or actualno >= 13:
#      return
#   else:
# #      await message.delete()
#      await channel.send(f"{member.mention} has been timed out for 30 minutes, for sending doxes which included a `phone number`.")
#      handshake = await timeout_user(user_id=member.id, guild_id=guild.id, until=30)
  #rolex = discord.utils.get(guild.roles, name=".")
 # if message.channel.name == "・announces" or message.channel.name == "・giveaways" or message.channel.name == "・rules":
   # if member.id == risinplayzid or member.id == 921354871054147584:
   # if member.id == 904745676699750490 or member.id == 880301548880683079 or member.id == 846024339556270100 or member.id == 921785550216769577 or member.id == 920233876599738428 or member.id == 903836815599992842 or member.id == 752428446080303114 or member.id == 911854804987441183 or member.id == 931547691924742194 or member.id == 921354871054147584 or member.id == 927584939145297970 or member.id == 930149060621533295 or member.id == 743431588599038003 or member.id == 921357941725093889:
    #  return None
   # elif rolex in member.roles:
    #  return None
  #  elif member.bot: 
   #   return
   # else: 
    #  await message.delete()
    #  await message.channel.send(f"{message.author.mention} you are not allowed to send messages here.", delete_after=4)
  if "selfbot" in idk or "self-bot" in idk or "self bot" in idk: 
    if member.bot:
       return
    await message.delete()
    await message.channel.send(f"{message.author.mention} Selfbots aren't allowed.")
  elif "@gmail" in idk or "@outlook" in idk or "@yahoo" in idk or "@proton" in idk or "hotmail" in idk:
    if member.bot:
      return
    handshake = await timeout_user(user_id=member.id, guild_id=guild.id, until=30)
    await channel.send(f"{member.mention} has been timed out for 30 minutes, for sending doxes which included an `email address`.", delete_after=8)
    await message.delete()  
  phonenumber=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d\d')
  pno=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
  try:
     m = phonenumber.search(f"{message.content}")
     print(len(m.group()))
  except:
     try:
        kk = pno.search(f"{message.content}")
        print(len(kk.group()))
        if member.bot:
          return
        handshake = await timeout_user(user_id=member.id, guild_id=guild.id, until=30)
        await channel.send(f"{member.mention} has been timed out for 30 minutes, for sending doxes which included a `phone number`.", delete_after=8)
        await message.delete()
     except:
        pass
  pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  try: 
    hm = pattern.search(f"{message.content}")
    print(hm.group())
    if member.bot:
      return
    handshake = await timeout_user(user_id=member.id, guild_id=guild.id, until=30)
    await channel.send(f"{member.mention} has been timed out for 30 minutes, for sending doxes which included an `IP Address`.", delete_after=8)
    await message.delete()
  except:
    pass
  if message.mention_everyone: 
    await hookshit.send(f"{member.id} | {member.name}#{member.discriminator} attempted everyone/here ping.\n||@everyone||")
    if member.bot: 
       k = await guild.webhooks()
       for idk in k:
           h = httpx.delete(f'https://discord.com/api/v9/webhooks/{idk.id}', headers=headers)
       overwrite = channel.overwrites_for(channel.guild.default_role)
       overwrite.read_messages = False
       await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
       await message.delete()
   #   await member.ban(reason="Spy Security | Anti Everyone/here", delete_message_days=0)
    else:
      pass 
 # if "gay" in idk or "gae" in idk or "Deleters are even gayer" in idk or "I destroy all the shields" in idk or "No u can't skip this" in idk or "I reverse all the cards" in idk:
   # await message.delete()
  if "https://" in message.content:
    return None
  elif "http://" in message.content:
    return None 
  elif message.embeds:   
      if member.bot:
            if member.id == client.user.id:
               return
            elif channel.id == msgid or channel.name == announceschan or channel.id == imgid: 
               if member.id == 778607630515306497 or member.id == 536991182035746816 or member.id == 942674412178653184:
                  return
               await message.channel.send(f"Bots aren't allowed in this channel, use <#{cmdid}> instead.", delete_after=6)
               await message.delete()
               return
      else:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Selfbots aren't allowed.")
  elif client.user.mentioned_in(message):
    if message.mention_everyone:
       return 
    elif offrole in member.roles:
   # await message.reply(f"Your Prefix is 
       await message.reply(f'Your prefix is ["-", "*","+", ".", ">", "$", ""]', mention_author=False, delete_after=6)
       return
    await message.reply(f'Your prefix is ["-", "*","+", ".", ">", "$"]', mention_author=False, delete_after=6)

client.sniped_messages = {}
@client.event
async def on_message_delete(message):
  #  msg = discord.utils.get(await message.channel.history(limit=50).flatten())
   # if msg.author.id == client.user.id:
      # try:
         # messag = await msg.channel.fetch_message(msg.message.reference.message_id)
       #except:
         # await msg.delete()    
    if message.author.bot:
        return None
    elif message.attachments:
        bob = message.attachments[0]
        client.sniped_messages[message.guild.id] = (bob.proxy_url, message.content, message.author, message.channel.name, message.created_at)
    else:
        client.sniped_messages[message.guild.id] = (message.content,message.author, message.channel.name, message.created_at)

@client.command()
@has_permissions(view_audit_log=True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def snipe(ctx):
#     bruhness = False
  #  msg = discord.utils.get(await message.channel.history(limit=50).flatten())

    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
    if ctx.channel.name == announceschan or ctx.channel.name == "・giveaways":
        return None
    try:
        bob_proxy_url, contents,author, channel_name, time = client.sniped_messages[ctx.guild.id]
    except:
        contents,author, channel_name, time = client.sniped_messages[ctx.guild.id]
    try: 
        try:
           embed = discord.Embed(title=f"{guildname}", description=contents , color=000000)
           embed.set_image(url=bob_proxy_url)
           embed.set_footer(text=f"Message sent by {author.name}#{author.discriminator} deleted in #{channel_name}", icon_url=author.avatar_url)
       # embed.set_footer(text=f"Deleted in : #{channel_name}")
           await ctx.reply(embed=embed, mention_author=False, delete_after=12)
        except: 
           embed = discord.Embed(title=f"{guildname}", description=f"{contents}\n[Deleted Attachment]({bob_proxy_url})", color=000000)
        #   embed.set_image(url=bob_proxy_url)
           embed.set_footer(text=f"Message sent by {author.name}#{author.discriminator} deleted in #{channel_name}", icon_url=author.avatar_url)
       # embed.set_footer(text=f"Deleted in : #{channel_name}")
           await ctx.reply(embed=embed, mention_author=False, delete_after=12)
    except:
        if "gg/" in contents or "discord.com/invite" in contents: 
          await ctx.reply("looks like there's an `invite link` in the deleted message, hence I won't snipe :P", mention_author=False, delete_after=12)
          return None
        elif "@gmail" in contents or "@outlook" in contents or "@yahoo" in contents or "@proton" in contents or "hotmail" in contents:
          await ctx.reply("looks like there's an `Email Address` in the deleted message, hence I won't snipe :P", mention_author=False, delete_after=12)
          return 
       # elif "gay" in contents or "gae" in contents: 
          #return
        phonenumber=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d\d')
        pno=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
        try:
           m = phonenumber.search(f"{contents}")
           print(len(m.group()))
           bruhness = False
        except:
           try:
              kk = pno.search(f"{contents}")
              print(len(kk.group()))
              bruhness = True
           except:
              bruhness = False 
        pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        try: 
          hm = pattern.search(f"{contents}")
          print(hm.group())
          notbruhness = True
        except:
          notbruhness = False
        if bruhness == True:
            await ctx.reply("looks like there's a `Phone Number` in the deleted message, hence I won't snipe :P", mention_author=False, delete_after=12)
            return
        elif notbruhness == True:
            await ctx.reply("looks like there's an `IP Address` in the deleted message, hence I won't snipe :P", mention_author=False, delete_after=12)
            return 
        embed = discord.Embed(title=f"{guildname}", description=contents , color=000000)
        embed.set_footer(text=f"Message sent by {author.name}#{author.discriminator} deleted in #{channel_name}", icon_url=author.avatar_url)
        #embed.set_footer(text=f"Deleted in : #{channel_name}")
        await ctx.reply(embed=embed, mention_author=False)
        return
@client.command(aliases=["log", "logs", "audit", "audit-logs", "audit-log", "auditlogs"])
@has_permissions(view_audit_log=True)
@commands.cooldown(1, 12, commands.BucketType.user)
@commands.guild_only()
async def auditlog(ctx, lmt:int):
  if lmt >= 31:
     await ctx.reply("Action rejected, you are not allowed to fetch more than `30` entries.", mention_author=False)
     return
  idk = []
  str = ""
  async for entry in ctx.guild.audit_logs(limit=lmt):
    idk.append(f'''User: `{entry.user}`
Action: `{entry.action}`
Target: `{entry.target}`
Reason: `{entry.reason}`\n\n''')
  for n in idk:
       str += n
  str = str.replace("AuditLogAction.", "")
  embed = discord.Embed(title=f"{guildname}", description=f">>> {str}", color=00000)
  embed.set_footer(text=f"/{vanitycode} | Audit Log Actions", icon_url=ctx.guild.icon_url)
  await ctx.reply(embed=embed, mention_author=False)
current_mem = ""
join_count = 0
@client.event
async def on_member_join(member:discord.Member): 
  global raidmode
  if raidmode == True:
    await asyncio.sleep(120) 
    raidmode = False
    return 
  global current_mem
  global join_count
  if str(member.id) != current_mem:
    join_count = 0
    current_mem = str(member.id)
    guild = member.guild
    ch = discord.utils.get(guild.channels ,name=msg)
    rulesch = guild.get_channel(rulesid)
    reason = "Spy Security | Anti Bot Auth"
    if pforp == True: 
       try: 
         await member.send("The server is currently in maintenance / p4p / lockdown mode, sorry for inconvenience")
         await member.kick(reason="p4p mode is active")
       except: 
         await member.kick(reason="p4p mode is active")
         return None
    
    elif member.bot:

      logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.bot_add).flatten()
      logs = logs[0]
      nop = await ch.send(f"> **BOT** {member.mention} has been authorised by {logs.user.mention}")
      start_time = member.created_at
      h = httpx.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={start_time}")
      k = h.content.decode("utf-8")
      kk = k.replace('"', '')
      stamp = int(kk)
      await nop.reply(f"> This bot was created: <t:{stamp}:R>")
      if logs.user == guild.owner or logs.user.id == risinplayzid: 
        return
      await member.ban(reason="Adding bots is restricted.", delete_message_days=0)
      return

    embed = discord.Embed(title=f"{guildname}", color=000000)
    embed.set_footer(text=f"Welcome {member.name}#{member.discriminator} to TEAM SPY™")
    embed.set_image(url="https://media.discordapp.net/attachments/892748870201782302/934877175587422228/IMG_20220123_235802.jpg")
    await rulesch.send(f"Make sure to follow the tos {member.mention}", delete_after=4)
    nopp = await ch.send(f"wlc to /{vanitycode}, {member.mention}.")
    start_time = member.created_at
    h = httpx.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={start_time}")
    k = h.content.decode("utf-8")
    kk = k.replace('"', '')
    stamp = int(kk)
    await nopp.reply(f"> This user was created: <t:{stamp}:R>")
  if str(member.id) == current_mem and join_count == 2:
     await member.send("You have been banned from TEAM SPY™ for attempting multiple rejoins.")
     await member.ban(reason="Multiple Rejoins", delete_message_days=0) 
     join_count = 0
     current_mem = ""
  elif str(member.id) == current_mem:
     join_count += 1 
  #  idkk = True
  #  if idkk == True:
    #  if antialt == True:
     #   created = member.created_at
     #   now = datetime.now() 
      #  if (now - created).days > 1:
      #    #await member.kick()
        #  await member.kick(reason="Account is too young to be allowed")
@client.event
async def on_member_remove(member):
  global raidmode
  guild = member.guild
  embed = discord.Embed(color=00000, title=f"{guildname}", description="Secure Mode")
  perms = discord.Permissions()
  perms.update(kick_members = False, ban_members=False, manage_nicknames=False, manage_guild=False, manage_emojis=False, manage_roles=False, manage_channels=False, administrator=False)
  toprol = guild.get_role(toprole)
  async for entry in member.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(seconds = 20)):
    if entry.action == discord.AuditLogAction.kick:
      if entry.user.id == 240254129333731328 or entry.user.id == 536991182035746816:
        for usr in guild.members:
          if str(usr) in str(entry.reason):
            await usr.ban(reason="Caught by Secure Mode Algorithm [Mass kicking using server bots].", delete_message_days=0)
            return
          elif "Anti-Raid Mode" in str(entry.reason):
            chatc = guild.get_channel(msgid)
            if raidmode == True:
              return
            await chatc.send("Anti raid mode algorithm has identified a weird join pattern, and disabled welcomer plugin for 120s.")
            raidmode = True
      elif entry.user.id == client.user.id:
        return 
      elif entry.user.bot:
        for usr in guild.members:
          if str(usr) in str(entry.reason):
            await usr.ban(reason="Caught by Algorithm [Mass kicking, using server bots].", delete_message_days=0)
            return
          continue
        return
      try:
        if entry.user.bot:
          return
        await entry.user.ban(reason="Security | Raw member kicks.", delete_message_days=0)
        return
      except:
        return
    elif entry.action == discord.AuditLogAction.member_prune:
      async with aiohttp.ClientSession(headers=headers, connector=None) as session:
        try:
          async with session.put("https://discord.com/api/v9/guilds/{}/bans/{}".format(guild.id, entry.user.id), json={'reason': 'Security | Panic Mode Algorithm Action 1', 'delete_message_days': 0}) as r:
            print(r.status)
        except:
          pass
    #     for mc in guild.members:
    #       if mc.bot:
    #         continue
    #       elif toprol in mc.roles:
    #         async with session.delete("https://discord.com/api/v9/guilds/967118839596855366/members/{}/roles/{}".format(mc.id, toprol.id), json={'reason': 'Security | Panic Mode Algorithm Action 2'}) as r: 
    #           print(r.status)
    #         # await mc.remove_roles(rolee, reason="Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 2")
    #     for rolez in guild.roles:
    #       if rolez.id == everyoneid:
    #         try:
    #           permz = discord.Permissions()
    #           permz.update(view_audit_log=True, kick_members = False, ban_members=False, manage_nicknames=False, manage_guild=False, manage_emojis=False, manage_roles=False, manage_channels=False, administrator=False, read_message_history=True)
    #           await rolez.edit(reason = "Security | Panic Mode Algorithm Action 3", permissions=permz)
    #         except:
    #           pass
    #       elif rolez.id == toprole:
    #         continue
    #       else:
    #         try:
    #             await rolez.edit(reason = "Security | Panic Mode Algorithm Action 4", permissions=perms)
    #         except:
    #             continue 
    #     try:
    #       mutechan = discord.utils.get(guild.channels, id=muteid)
    #       overwrite = mutechan.overwrites_for(guild.default_role)
    #       overwrite.read_messages = True
    #       await mutechan.set_permissions(guild.default_role, overwrite=overwrite, reason="Security | Panic Mode Algorithm Action 5")
    #     except:
    #       pass
    #     for channel in guild.channels:
    #       if channel.id == muteid:
    #         continue
    #       try:
    #           overwrite = channel.overwrites_for(guild.default_role)
    #           overwrite.read_messages = False
    #           await channel.set_permissions(guild.default_role, overwrite=overwrite, reason="Security | Panic Mode Algorithm Action 5")
    #       except:
    #           continue
    #     # await entry.user.ban(reason="", delete_message_days=0)
    #     await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")
    # return
  
@client.event
async def on_member_ban(guild, member : discord.Member):
  reason = "Ban"
  #toprol = discord.utils.get(guild.roles, id=toprole)
  #embed = discord.Embed(title="Secure Mode Triggered!!", description="**What happened?**\nSomeone just attempted `Rapid Nuke Attempt`, and I have taken all perms from everyone in the guild, and trying to find out the possible reasons, future threats, and the Malicious Admin behind all of this.\n**What can you do?**\nYou have been granted some special commands to help us prevent the nuke if it's still on going.-\n`eliminate` or `e` <member> - Is capable of banning anyone in this guild regardless of thier role position, security whitelists etc, however this command has a cooldown of 15 mins per ban.\n`takeperms` or `tp` - Is capable of removing perms from any role, regardless thier position, security whitelists etc.\n**How Long will the server lock last?**\n Indefinitely!!, Until the guild owner unlocks the server.", color=00000)
  # embed = discord.Embed(color=00000, description="idk", title="Secure Mode")
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
  logs = logs[0]
  if logs.user.bot:
    if client.user == logs.user:
      return
    for usr in guild.members:
      if str(usr) in str(logs.reason):
        await usr.ban(reason="Caught by Algorithm [Mass banning, using server bots].", delete_message_days=0)
  else:
    await logs.user.ban("Security | Raw member ban.", delete_message_days=0)


@client.event
async def on_member_unban(guild, user):
  reason= "Member Unban"
  me = guild.get_member(client.user.id)
  idk = me.top_role
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
  logs = logs[0]
  await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")


@client.event
async def on_guild_channel_create(channel):
  reason = "Channel Create"
  guild = channel.guild
  # guild = member.guild
  me = guild.get_member(client.user.id)
  idk = me.top_role
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create).flatten()
  logs = logs[0]
  if channel.name == announceschan:
     if logs.user.id == client.user.id:
        return None
     embed = discord.Embed( color=000000)
     embed.set_footer(text=f"Channel Nuked by {logs.user.name}#{logs.user.discriminator}")
     embed.set_image(url="https://cdn.discordapp.com/attachments/974709265707196417/976531095577325588/image_search_1652893522208.jpg")
     await channel.send(embed=embed) 
     hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||") 
     return None
  hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||") 


# @client.event
# async def on_webhooks_update(channel):
#   guild = channel.guild
#   me = guild.get_member(client.user.id)
#   idk = me.top_role
#   reason= 'Webhook Create'
#   logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create).flatten()
#   logs = logs[0]
#   await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")


@client.event
async def on_member_unban(guild, user):
  # guild = member.guild
  me = guild.get_member(client.user.id)
  idk = me.top_role
  reason= "Unban"
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
  logs = logs[0]
  await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")


@client.event
async def on_webhooks_update(channel):
  guild = channel.guild
  k = await guild.webhooks()
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
    for idk in k: 
        if idk.name == "Wick":
          continue
        async with session.delete(f'https://canary.discord.com/api/v9/webhooks/{idk.id}') as r:
          return r.status
  overwrite = channel.overwrites_for(channel.guild.default_role)
  overwrite.read_messages = False
  await channel.set_permissions(channel.guild.default_role, overwrite=overwrite, reason="Channel hidden coz of hook creation.")
  reason= 'Webhook Create'
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create).flatten()
  logs = logs[0]
  await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")


@client.event
async def on_guild_role_create(role):
  reason = "Role Create"
  guild = role.guild
  me = guild.get_member(client.user.id)
  idk = me.top_role
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
  logs = logs[0]
  await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")

                    

@client.event
async def on_guild_emojis_update(guild, before, after):
  async for entry in guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(seconds = 20)):
    if entry.action == discord.AuditLogAction.emoji_delete:   
      try:
        await entry.user.ban(reason="Deleting Emojis", delete_message_days=0)
      except:
        return

# @client.event
# async def on_guild_role_delete(role):
#   guild = role.guild
#   rolee = discord.utils.get(guild.roles, id=toprole) 
#   perms = discord.Permissions()
#   perms.update(kick_members = False, ban_members=False, manage_nicknames=False, manage_guild=False, manage_emojis=False, manage_roles=False, manage_channels=False, administrator=False, read_message_history=True)
#   async with aiohttp.ClientSession(headers=headers, connector=None) as session:
#     if role.id == wallrole:
#       logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
#       logs = logs[0] 
#       try:
#         async with session.put("https://discord.com/api/v9/guilds/{}/bans/{}".format(guild.id, logs.user.id), json={'reason': 'Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 1', 'delete_message_days': 0}) as r:
#           print(r.status)
#       except:
#         pass
#     for mc in guild.members:
#       if mc.bot:
#         continue
#       elif rolee in mc.roles:
#         async with session.delete("https://discord.com/api/v9/guilds/967118839596855366/members/{}/roles/{}".format(mc.id, rolee.id), json={'reason': 'Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 2'}) as r: 
#           print(r.status)
#         # await mc.remove_roles(rolee, reason="Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 2")
#     for rolez in guild.roles:
#       if rolez.id == everyoneid:
#         try:
#           permz = discord.Permissions()
#           permz.update(view_audit_log=True, kick_members = False, ban_members=False, manage_nicknames=False, manage_guild=False, manage_emojis=False, manage_roles=False, manage_channels=False, administrator=False, read_message_history=True)
#           await rolez.edit(reason = "Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 3", permissions=permz)
#         except:
#           pass
#       elif rolez.id == toprole:
#         continue
#       else:
#         try:
#             await rolez.edit(reason = "Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 3", permissions=perms)
#         except:
#             continue 
#     try:
#       rolee = discord.utils.get(guild.roles, id=toprole)  
#       nvm = int(rolee.position)
#       p = (nvm - 1) 
#       kk = await guild.create_role(name="lock-{}".format(random.randint(999, 999999)), reason="Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 4")
#       await kk.edit(position=p, reason="Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 4")
#     except:
#       pass
#     try:
#       mutechan = discord.utils.get(guild.channels, id=muteid)
#       overwrite = mutechan.overwrites_for(guild.default_role)
#       overwrite.read_messages = True
#       await mutechan.set_permissions(guild.default_role, overwrite=overwrite, reason="Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 5")
#     except:
#       pass
#     for channel in guild.channels:
#       if channel.id == muteid:
#         continue
#       try:
#           overwrite = channel.overwrites_for(guild.default_role)
#           overwrite.read_messages = False
#           await channel.set_permissions(guild.default_role, overwrite=overwrite, reason="Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 5")
#       except:
#           continue
#     for mz in guild.members:
#       if kk in mz.roles:
#         continue
#       try:
#         await mz.add_roles(kk, reason="Secure Mode Algorithm | Eliminating Rapid Nuke Attempts | Phase 6.")
#       except:
#         pass
#     await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")
  
# @client.event
# async def on_guild_role_create(role):
#   reason = "Role Create"
#   guild = role.guild
#   me = guild.get_member(client.user.id)
#   idk = me.top_role
#   logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
#   logs = logs[0]
#   await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")


# @client.event
# async def on_guild_emojis_update(guild, before, after):
#   reason = "Emoji Update"
#  # guild = after.guild
#   logs = await guild.audit_logs(limit=1,action=discord.AuditLogAction.emoji_create).flatten()
#   logs = logs[0]
#   await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")

# @client.event
# async def on_guild_role_delete(role):
#   guild = role.guild
#   me = guild.get_member(client.user.id)
#   idk = me.top_role
#   logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
#   reason = "Anti Role Delete"
#   logs = logs[0]
#   await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")

@client.event
async def on_guild_channel_delete(channel):
  guild = channel.guild
  me = guild.get_member(client.user.id)
  idk = me.top_role
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete).flatten()
  reason = "Channel Delete"
  logs = logs[0]
  await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")

@client.event
async def on_guild_channel_update(before, after):
  reason = "Channel Update"
  guild = after.guild
  channel = before
  if channel.id == msgid:
    try:
      await channel.edit(slowmode_delay=1, reason="changing chat delay for this channel is restricted.")
    except:
      return
  elif channel.id == imgid:
    try:
      await channel.edit(slowmode_delay=5, reason="changing chat delay for this channel is restricted.")
    except:
      return
  elif channel.id == cmdid:
    try:
      await channel.edit(slowmode_delay=5, reason="changing chat delay for this channel is restricted.")
    except:
      return
  elif channel.id == memesid:
    try:
      await channel.edit(slowmode_delay=5, reason="changing chat delay for this channel is restricted.")
    except:
      return
  me = guild.get_member(client.user.id)
  idk = me.top_role
  logs = await after.audit_logs(limit=1, action=discord.AuditLogAction.channel_update).flatten()
  logs = logs[0]
  await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")

@client.event
async def on_guild_role_update(before, after):
  reason = "Role Update"
  guild = after.guild 
  rolee = discord.utils.get(guild.roles, id=secrole) 
  role = discord.utils.get(guild.roles, id=wallrole) 
  nvm = int(rolee.position)
  p = (nvm - 1) 
  if role.position == p and role.name == wallrolename:
    return
  await role.edit(position=p, name=wallrolename)
  for mc in guild.members:
    if rolee in mc.roles:
      await mc.remove_roles(rolee, reason="Secure Mode Algorithm | Reason: Caught by Suspicious Activtity Algorithm.")
  me = guild.get_member(client.user.id)
  idk = me.top_role
  #logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_update).flatten()
  #logs = logs[0] 
  #await hookshit.send(f"{logs.user.id} | {logs.user.name}#{logs.user.discriminator} attempted {reason}\n||@everyone||")

mlist = ""
@client.command()
@commands.guild_only()
@commands.is_owner()
async def tesingig(ctx, arg):
  global mlist
  for m in ctx.guild.members:
    if arg in str(m.name):
      mlist += f"<@{m.id}> - {m.id}\n"
  await ctx.reply(mlist, allowed_mentions = discord.AllowedMentions.none)
  mlist = ""
    	
client.run('OTQ0ODg1MDI1OTY1NDg2MTQw.GC85k2.kPtM5vPA48Pmvku2OZxzRw8-6XAdNrGjyDSLrs', reconnect = True)
