"""
Created By @Jisan7509
Modified @Akarata
GF created by @KshitijGagan
"""
import asyncio
import random

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, catmemes


@bot.on(admin_cmd(outgoing=True, pattern="abuse$"))
@bot.on(sudo_cmd(pattern="abuse$", allow_sudo=True))
async def abusing(abused):
    reply_text = random.choice(catmemes.ABUSE_STRINGS)
    await edit_or_reply(abused, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="abusehard$"))
@bot.on(sudo_cmd(pattern="abusehard$", allow_sudo=True))
async def fuckedd(abusehard):
    reply_text = random.choice(catmemes.ABUSEHARD_STRING)
    await edit_or_reply(abusehard, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="rendi$"))
@bot.on(sudo_cmd(pattern="rendi$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(catmemes.RENDISTR)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(outgoing=True, pattern="fuck$"))
@bot.on(sudo_cmd(pattern="fuck$", allow_sudo=True))
async def chutiya(fuks):
    reply_text = random.choice(catmemes.CHU_STRINGS)
    await edit_or_reply(fuks, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="thanos$"))
@bot.on(sudo_cmd(pattern="thanos$", allow_sudo=True))
async def thanos(thanos):
    reply_text = random.choice(catmemes.THANOS_STRINGS)
    await edit_or_reply(thanos, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern=f"gf$"))
@bot.on(sudo_cmd(pattern=f"gf$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(21)
    kakashi = await edit_or_reply(event, "BSDK tera gf h na ek ...!")
    animation_chars = [
        "`Ruk jaa , Abhi teri GF ko Fuck karta hu `",
        "`Making your Gf warm 🔥`",
        "`Pressing her boobs 🤚😘`",
        "`Stimulating her pussy🖕`",
        "`Fingering her pussy 💧😍👅 `",
        "`Asking her to taste my DICK🍌`",
        "`Requested accepted😻💋, Ready to taste my DICK🍌`",
        "`Getting her ready to fuck 👀`",
        "`Your GF Is Ready To Fuck`",
        "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nTrying new SEX position to make her Squirt\n\nAlmost Done. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get White\nShe squirted like a shower💧💦👅\n\nAlmost Done..\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nDoing Extreme SEX with her👄\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nWarming her Ass🍑 to Fuck!🍑🍑\n\nAlmost Done....\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\nInserted my Penis🍌 in her ASS🍑\n\nAlmost Done.....\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\ndoing extreme sex with her\n\nAlmost Done......\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nPressing her tight Nipples🤚👀\n\nAlmost Done.......\n\nFucked Percentage... 84%\n███████████████████▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Lips Get Horny\nDoing French Kiss with your GF👄💋\n\nAlmost Done........\n\nFucked Percentage... 89%\n██████████████████████▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nI am getting ready to cum in her Mouth👄\n\nAlmost Done.......\n\nFucked Percentage... 90%\n██████████████████████▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nFinally, I have cummed in her Mouth👅👄\n\nAlmost Done.......\n\nFucked Percentage... 96%\n████████████████████████▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's is Awesome\nShe is Licking my Dick🍌 in the Awesome Way✊🤛🤛👅👄\n\nAlmost Done.......\n\nFucked Percentage... 100%\n█████████████████████████ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\nCummed On her Mouth👅👄\n\nYour GF got Pleasure\n\nResult: Now I Have 1 More SEX Partner 👍👍`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 21])


@bot.on(admin_cmd(outgoing=True, pattern="fk (.*)"))
@bot.on(sudo_cmd(pattern="fk (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    animation_interval = 3
    animation_ttl = range(11)
    kakashi = await edit_or_reply(event, "👁👁")
    animation_chars = [
        f"👁👁\n  👄  =====> Aku {name} Cium",
        f"👁👁\n  👅  =====> Aku {name} Sepong",
        f"👁👁\n  💋  =====> Aku {name} Sepong",
        f"👁👁\n  👄  =====> Aku {name} Cium",
        f"👁👁\n  💋  =====> Aku {name} Sepong",
        f"👁👁\n  👄  =====> Aku {name} Cium",
        f"👁👁\n  👅  =====> Aku {name} Crooot",
        f"👁👁\n  💋  =====> Aku {name} Sepong lagi",
        f"👁👁\n  👄  =====> Aku {name} Cium",
        f"👁👁\n  👅  =====> Aku {name} Croot",
        f"👁👁\n  👄  =====> Hai {name} Apakah kamu ingin lagi?...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])


@bot.on(admin_cmd(outgoing=True, pattern=f"chod$"))
@bot.on(sudo_cmd(pattern=f"chod$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(11)
    kakashi = await edit_or_reply(event, "1 2 3..Searching Randi..")
    animation_chars = [
        "`Randi Founded`",
        "`Your Mom Is Going To Fuck`",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 84%\n█████████████████████▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 100%\n█████████████████████████ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nYour mom get Pregnant\n\nResult: Now You Have 1 More Younger Brother `",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])


@bot.on(admin_cmd(outgoing=True, pattern=f"rape$"))
@bot.on(sudo_cmd(pattern=f"rape$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(30)
    kakashi = await edit_or_reply(event, "repe")
    animation_chars = [
        "**r**",
        "**ra**",
        "**rap**",
        "**rape**",
        "**rape_**",
        "**rape_t**",
        "**rape_tr**",
        "**rape_tra**",
        "**rape_trai**",
        "**rape_train**",
        "**ape_train🚅**",
        "**pe_train🚅🚃🚃**",
        "**e_train🚅🚃🚃🚃**",
        "**_train🚅🚃🚃🚃🚃**",
        "**train🚅🚃🚃🚃🚃🚃**",
        "**rain🚅🚃🚃🚃🚃🚃🚃**",
        "**ain🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**in🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**n🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**rApEd**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 30])


@bot.on(admin_cmd(outgoing=True, pattern="kiss$"))
@bot.on(sudo_cmd(pattern="kiss$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="fuk$"))
@bot.on(sudo_cmd(pattern="fuk$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="sex$"))
@bot.on(sudo_cmd(pattern="sex$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern=f"nakal$"))
@bot.on(sudo_cmd(pattern=f"nakal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    kakashi = await edit_or_reply(event, "nakal")
    animation_chars = [
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Lavde   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pehli   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(P)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Fursat  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Meeee   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀lodu⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 6])


@bot.on(admin_cmd(outgoing=True, pattern="gaali$"))
@bot.on(sudo_cmd(pattern="gaali$", allow_sudo=True))
async def cat(event):
    await edit_or_reply(
        event,
        "Madarchod Randi ke bacche Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI !",
    )


@bot.on(admin_cmd(outgoing=True, pattern="gali$"))
@bot.on(sudo_cmd(pattern="gali$", allow_sudo=True))
async def cat(event):
    await edit_or_reply(
        event,
        "Behen ke lode madahrchod teri ma randi bhsdk tera pyra khandan randi teri kandan kai ma ka bhods lund katta madarchod tere lund pe road roller chale tere behen ki chut kate tura khandan ke gand me bomb phute teri ma ke bur me 100 log ke lund teri behen ke bur me 100 log ke lund madarchod behenchod mai ka loda behen ka loda randi teri behen ma ki chut behen ki chut teri chut ki chut harami phate hue condom ke nateeje tera baap ko paisa nahi tha to uses condom se teri maa ko chooda benchod lodo hai tu sabka chusta gay lund hai nahi be lund akuad me re hamare desh ki taraf bhi dekha to tatte ukhad ke kutto ko keladenge madharchod Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI loda leke muh me nachne wale ma ki jaat lund kate tera tiri bb ko chode duniya tiri gand me parmanu dhamaka teri ma ka buur me garam oil ki kadhai teri behen ki bane porn aur upload ho pornhub me teri ma ko 100 logo ne choda tab tu paida hua tra papa gay tu gay tera khandan gay bc mc maki chut belen ki lodi ma ki lodi behen teri randi ma teri randi loda undono ke muh me loda katgaya to muh me lele aur kuch hame bola to tera loda tere muh me deke tere gand se nikalenge madarchod beti teru chodaye beti teri rundi teri beti ki bur me 1000 logo ka lund teri beti ka gangbang tere papa be lund nund na hone ke karan teri ma rundi teri ma randi hone ke karan tu aur tera bhai behen teri behen radi kuki teri ma randi behen radi hone ke karan ro 1000 se choda ke uske 10000 bacche tere lund par hathi dore teri gand me chiti kate kera pura satyanash ho *Main roz teri* *behno ki banjar chut me* *apna lawda daalke andar* *haryali lata tha magar aaj* *unke ke baare me* *sunke mujhe bhut afsos* *huwa..ki unko ab bada loudha chahye..ab mera balatkaaari* *lawda lagataar 4 ghante tk* *apne muh me kon* *rakhega..vo teri* *behne hi thi jo apni kaali* *magar rasilli chut mere* *saamne khol deti aur* *zameen pe naagin ki tarah* *rengne lgti thi jaise ki* *kisine unki chut pe naariyal* *tod diya ho vo b bada wala* *mumbai ka naariyal.",
    )


@bot.on(admin_cmd(outgoing=True, pattern="ngntd$"))
@bot.on(sudo_cmd(pattern="ngntd$", allow_sudo=True))
async def cat(event):
    await edit_or_reply(
        event,
        "Ini untuk lu, lu adalah tempat ngentd gw tidak tahu mengapa orang tua lu melahirkan anak yang tidak berharga seperti lu, lu banci dengan seorang anak gay yang cerewet dan sangean  hahaha lu seperti babi,  Sial beritahu bapa lu untuk meniduri lu setiap malam sehingga lu dapat membuat mmk lu lebih efektif untuk semua orang yang telah menidurilu sampai sekarang omong kosong berkata di depan mata semua orang seperti lu minum kencing kucing pada saat yang sama sambil menghisap kntl bleh 😂  haha 😂😂😂😂  apa yang lu pikir mungkin lu pikir seperti gw dari mars? Gw bukan dan itulah mengapa gw terisolasi darilu ya tahu apa mmk lu yang enak, lu akan disetubuhi lagi oleh kucing ini  tunggu saja anak jamet dengan penis palsu sialan 😂😂😂😂😂😂😂😂😂 ngentd sama lu🖕gw akan datang lagi dan lagi untuk bercinta dengan lu setiap kali lu berada di depan mata gw, gw akan berada di sana untuk ngentd  mmk lu hahah…    )

CMD_HELP.update(
    {
        "sange": "__**NAMA PLUGIN :** Sange__\
\n\n✅** CMD ➥** `.fk` <teks>\
\n**Fungsi   ➥  **Beri seseorang sange.\
\n\\n✅** CMD ➥** `.ngntd` |`.abuse` | `.abusehard` | `.rendi` | `.fuck` | `.thanos` | `.gf` | `.chod` | `.rape` | `.kiss` | `.fuk` | `.sex` | `.nakal` | `.gaali` | `.gali` \
\n\n**Fungsi   ➥  **apa kau sudah mendapatkannya!  Tidak?.\
"
    }
)
