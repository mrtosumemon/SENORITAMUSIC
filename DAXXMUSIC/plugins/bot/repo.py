from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ ωεℓ¢σмє ƒσя 𝑱𝑨𝑹𝑽𝑰𝑺 яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/BWANDARLOK"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/jarvis2O"),
          ],
               [
                InlineKeyboardButton("𝗟𝗜𝗩𝗘 𝗖𝗖", url="https://t.me/OXY474_STORE"),

],
[
              InlineKeyboardButton("𝐀𝐋𝐋 𝐁𝐎𝐓𝐒", url=f"https://t.me/CDX_WORLD"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/doraemon890/jarvisXmusic"),
              ],
              [
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎", url=f"https://github.com/PRADHAN474/managerbot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/PRADHAN474/Oxychatbot"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://github.com/doraemon890/jarvisXsession-for-both-pyro"),
InlineKeyboardButton("𝐁𝐖𝐀𝐍𝐃𝐀𝐑𝐋𝐎𝐊", url=f"https://t.me/BWANDARLOK"),
],
[
              InlineKeyboardButton("𝐆𝐈𝐓𝐇𝐔𝐁 𝐏𝐑𝐎𝐅𝐈𝐋𝐄", url=f"https://github.com/doraemon890"),
              InlineKeyboardButton("𝐃𝐎𝐑𝐀𝐄𝐌𝐎𝐍♡︎", url=f"https://t.me/Doraemon890"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗕𝗢𝗧 𝗩2", url=f"https://github.com/doraemon890/JarvisStringSessionBot"),
InlineKeyboardButton("𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧", url=f"https://github.com/PRADHAN474/BROADCAST"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/PRADHAN474/OXYUSERBOT"),
InlineKeyboardButton("𝐂𝐎𝐃𝐄𝐗", url=f"https://t.me/TEAM_CDX"),
],
[
InlineKeyboardButton("𝗔𝗟 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧", url=f"https://github.com/doraemon890/Jarvis-X-spam"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/58afe55fee5ae99d6901b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
