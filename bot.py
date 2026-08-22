import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Salom! Men MelvixFindBot.\n\n"
        "Menga:\n"
        "🎧 musiqa nomi yoki ijrochini\n"
        "🎙 ovozli xabarni\n"
        "🎬 dumaloq videoni\n"
        "📎 Instagram Reels havolasini\n\n"
        "yuboring — musiqani topishga yordam beraman."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⏳ Qabul qilindi! Hozircha botning asosiy tizimini sozlayapmiz."
    )

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN topilmadi!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    print("MelvixFindBot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
