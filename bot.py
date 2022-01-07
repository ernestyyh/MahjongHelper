import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from mahjongHandler.mahjonghand import MahjongHand
from mahjongHandler.mahjonghandanalyser import MahjongHandAnalyser

def start(update, context):
    update.message.reply_text(
        "Send a photo of your tiles and I will tell you how close you are to a winning hand.\n"
    )

def help_command(update, context):
    update.message.reply_text(
        "Please send the photos of tiles."
    )

def load_model():
    global model
    # model = load the model here

def detect_tiles(update, context):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')

    tiles = model.predict('user_photo.jpg')[0]
    hand = MahjongHand(tiles)

    analyser = MahjongHandAnalyser()
    results = analyser.analyser(hand)
    tiles_to_keep = results[0]
    tiles_to_discard = results[1]
    missing_tiles = results[2]

    tiles_to_keep_str = "These are the tiles to keep " + " ".join(tiles_to_keep)
    tiles_to_discard_str = "These are the tiles to discard " + " ".join(tiles_to_discard)
    missing_tiles_str = "These are the missing tiles " + " ".join((missing_tiles))

    update.message.reply_text(
        tiles_to_keep_str + "\n" +
        tiles_to_discard_str + "\n" +
        missing_tiles_str
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