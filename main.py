from pyrogram import Client, filters
from pyrogram.types import Message
import os
import re
from pyromod import listen
import requests
import json
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from logger import logging
import time
import asyncio
from config import api_id, api_hash, bot_token, auth_users, sudo_users

app = Client("Ravidrmbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command(["start"]))
async def start_command(client: Client, message: Message):
    await message.reply("Bot start ho gaya hai!")


@app.on_message(filters.document)
async def document_handler(client: Client, message: Message):
    file_id = message.document.file_id
    file_name = message.document.file_name
    await message.reply("File download ho raha hai...")
    await client.download_media(file_id, file_name)
    await message.reply("File download ho gaya hai!")


@app.on_message(filters.command(["extract"]))
async def extract_command(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply("❌ Kripya kisi file ko reply karke /extract command do.")
        return

    await message.reply("Links extract kar raha hoon...")
    file_path = await client.download_media(message.reply_to_message.document.file_id)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Just a placeholder - you can extract links as needed from content
    links = re.findall(r'https?://\S+', content)

    if links:
        await message.reply(f"🔗 {len(links)} links mile:\n\n" + "\n".join(links[:10]))
    else:
        await message.reply("❌ Koi valid link nahi mila.")

# Start the bot
app.run()
