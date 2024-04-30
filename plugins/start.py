# Copyright 2023 Qewertyy, MIT License

from pyrogram import Client, filters, types as t
from bot import StartTime

startText = """
Ai Utility Bot By @NandhaBots
Commands:
`/draw`: create images
`/upscale`: upscale your images
`/gpt`: chatgpt
`/bard`: bard ai by google
`/mistral`: mistral ai
`/llama`: llama by meta ai
`/palm`: palm by google
`/reverse`: reverse image search
`/gemini`: gemini by google

Powered By Lexica Api
"""

@Client.on_message(filters.command(["start","help","repo","source"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText,
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="Credits & Source",url="https://github.com/Qewertyy/SDWaifuRobot")
                ]
            ]
        )
    )
