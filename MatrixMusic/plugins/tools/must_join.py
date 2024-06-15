from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from MatrixMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/KKC8C":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("KKC8C", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/KKC8C".isalpha():
                link = "https://t.me/KKC8C"
            else:
                chat_info = await bot.get_chat("kkc8c")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ حَبيبي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البوت .\n⌯︙قناة : t.me/KKC8C 🍓.\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("𝗕𝗟𝗔𝗖𝗞 |⌯𖤒˼ ˹🖤˼", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat @KKC8C !")
