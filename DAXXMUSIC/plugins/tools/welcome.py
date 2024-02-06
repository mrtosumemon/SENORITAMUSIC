from DAXXMUSIC import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from DAXXMUSIC.utils.daxx_ban import admin_filter


random_photo = [
    "https://telegra.ph/file/3a35b86005e7b3c2d9310.jpg",
    "https://telegra.ph/file/2e7b72279b28105607667.jpg",
    "https://telegra.ph/file/87bae0c629ae73032ae77.jpg",
    "https://telegra.ph/file/f85e89871eb80c91f8a87.jpg",
    "https://telegra.ph/file/70c87e971a919a48e3e2b.jpg",
]
# --------------------------------------------------------------------------------- #

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #

def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname):
    background = Image.open("DAXXMUSIC/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((825, 824))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('DAXXMUSIC/assets/font.ttf', size=110)
    welcome_font = ImageFont.truetype('DAXXMUSIC/assets/font.ttf', size=60)
    draw.text((2100, 1420), f'ID: {id}', fill=(12000, 12000, 12000), font=font)
    pfp_position = (1990, 435)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"

# Function to handle new members
async def handle_member_update(client: app, member: ChatMemberUpdated):
    chat = member.chat
    
    count = await app.get_chat_members_count(chat.id)
   
    if member.new_chat_member:
        user = member.new_chat_member.user
        try:
            if user.photo:
                # User has a profile photo
                photo = await app.download_media(user.photo.big_file_id)
                welcome_photo = await get_userinfo_img(
                    bg_path=bg_path,
                    font_path=font_path,
                    user_id=user.id,
                    profile_path=photo,
                )
            else:
                # User doesn't have a profile photo, use random_photo directly
                welcome_photo = random.choice(random_photo)

            # Welcome message for new members
            caption = (
            f"**🌷ʜᴇʏ ✧ {member.new_chat_member.user.mention}**\n\n**🏘Wᴇʟᴄᴏᴍᴇ Tᴏ🥳**\n\n"
            f"**📝** {chat.title}\n"
            f"**🔐ʟɪɴᴋ ✧ @{chat.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**๏ ᴍᴇᴍʙᴇʀ Iᴅ ✧** `{member.new_chat_member.user.id}`\n"
            f"**๏ ᴜsᴇʀɴᴀᴍᴇ ✧ @{member.new_chat_member.user.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**👥ᴛᴏᴛᴀʟ Mᴇᴍʙᴇʀ Nᴏᴡ ✧ {count}**"
            )
            button_text = "๏ ᴠɪᴇᴡ ɴᴇᴡ ᴍᴇᴍʙᴇʀ ๏"
            add_button_text = "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏"

            # Generate a deep link to open the user's profile
            deep_link = f"tg://openmessage?user_id={user.id}"
            add_link = f"https://t.me/{app.username}?startgroup=true"

            # Send the message with the photo, caption, and button
            await client.send_photo(
                chat_id=member.chat.id,
                photo=welcome_photo,
                caption=caption,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)],
                    [InlineKeyboardButton(text=add_button_text, url=add_link)],
                ])
            )
        except RPCError as e:
            print(e)

# Connect the function to the ChatMemberUpdated event
@app.on_chat_member_updated(filters.group, group=10)
async def member_update_handler(client: app, member: ChatMemberUpdated):
    await handle_member_update(client, member)
