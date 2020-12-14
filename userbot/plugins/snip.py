# ported from paperplaneExtended by avinashreddy3108 for media support

from telethon import events

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import BOTLOG_CHATID, CMD_HELP, cat_users
from .sql_helper.snip_sql import add_note, get_note, get_notes, rm_note


@bot.on(events.NewMessage(pattern=r"\#(\S+)", from_users=cat_users))
async def incom_note(getnt):
    try:
        if not (await getnt.get_sender()).bot:
            notename = getnt.text[1:]
            note = get_note(notename)
            message_id_to_reply = getnt.message.reply_to_msg_id
            if not message_id_to_reply:
                message_id_to_reply = None
            if note:
                if note.f_mesg_id:
                    msg_o = await bot.get_messages(
                        entity=BOTLOG_CHATID, ids=int(note.f_mesg_id)
                    )
                    await getnt.delete()
                    await bot.send_message(
                        getnt.chat_id,
                        msg_o,
                        reply_to=message_id_to_reply,
                        link_preview=False,
                    )
                elif note.reply:
                    await getnt.delete()
                    await bot.send_message(
                        getnt.chat_id,
                        note.reply,
                        reply_to=message_id_to_reply,
                        link_preview=False,
                    )
    except AttributeError:
        pass


@bot.on(admin_cmd(pattern=r"snips (\w*)"))
@bot.on(sudo_cmd(pattern=r"snips (\w*)", allow_sudo=True))
async def add_snip(fltr):
    keyword = fltr.pattern_match.group(1)
    string = fltr.text.partition(keyword)[2]
    msg = await fltr.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await bot.send_message(
                BOTLOG_CHATID,
                f"#NOTE\
                  \nKEYWORD: `#{keyword}`\
                  \n\nThe following message is saved as the snip in your bot , do NOT delete it !!",
            )
            msg_o = await bot.forward_messages(
                entity=BOTLOG_CHATID, messages=msg, from_peer=fltr.chat_id, silent=True
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                fltr,
                "Menyimpan media sebagai data untuk catatan membutuhkan `PRIVATE_GROUP_BOT_API_ID` disetel.",
            )
            return
    elif fltr.reply_to_msg_id and not string:
        rep_msg = await fltr.get_reply_message()
        string = rep_msg.text
    success = "Catatan {}  berhasil disimpan. Use` #{} `to get it"
    if add_note(keyword, string, msg_id) is False:
        rm_note(keyword)
        if add_note(keyword, string, msg_id) is False:
            return await edit_or_reply(
                fltr, f"Kesalahan dalam menyimpan snip yang diberikan {keyword}"
            )
        return await edit_or_reply(fltr, success.format("updated", keyword))
    return await edit_or_reply(fltr, success.format("added", keyword))


@bot.on(admin_cmd(pattern="snipl$"))
@bot.on(sudo_cmd(pattern=r"snipl$", allow_sudo=True))
async def on_snip_list(event):
    message = "Tidak ada catatan yang disimpan dalam obrolan ini"
    notes = get_notes()
    for note in notes:
        if message == "Tidak ada catatan yang disimpan dalam obrolan ini":
            message = "Catatan disimpan dalam obrolan ini:\n"
        message += "👉 `#{}`\n".format(note.keyword)
    if len(message) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(message)) as out_file:
            out_file.name = "snips.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Catatan Tersedia",
                reply_to=event,
            )
            await event.delete()
    else:
        await edit_or_reply(event, message)


@bot.on(admin_cmd(pattern=r"snipd (\S+)"))
@bot.on(sudo_cmd(pattern=r"snipd (\S+)", allow_sudo=True))
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    catsnip = get_note(name)
    if catsnip:
        rm_note(name)
    else:
        return await edit_or_reply(
            event, f"Are you sure that #{name} is saved as snip?"
        )
    await edit_or_reply(event, "snip #{} deleted successfully".format(name))


CMD_HELP.update(
    {
        "snip": "__**NAMA PLUGIN :** Snip__\
\n\n✅** CMD ➥**  #<nama catatan>\
\n**Fungsi   ➥  **Mendapat catatan tertentu.\
\n\n✅** CMD ➥** `.snips`: membalas pesan dengan `.snips <nama catatan>`\
\n**Fungsi   ➥  **Menyimpan pesan yang dibalas sebagai catatan dengan notename.(Bekerja dengan foto, dokumen, dan stiker juga!)\
\n\n✅** CMD ➥** `.snipl`\
\n**Fungsi   ➥  **Mendapat semua catatan yang disimpan dalam obrolan.\
\n\n✅** CMD ➥** `.snipd <nama catatan>`\
\n**Fungsi   ➥  **Menghapus catatan tertentu.\
"
    }
)
