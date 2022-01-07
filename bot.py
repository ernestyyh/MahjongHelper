import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text(
        "start message"
    )

def help_command(update, context):
    update.message.reply_text(
        "help message"
    )

def detect_tiles(update, context):
    update.message.reply_text(
        "detect tiles message"
    )

def main():
    updater = Updater(token="5055147777:AAF2TLDAhAtZCPN9HFryiiH64_51Rta9q98", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.photo, detect_tiles))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()