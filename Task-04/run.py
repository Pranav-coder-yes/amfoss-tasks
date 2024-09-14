from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7476072047:AAGvdy2SoJki3_Z1YFB30wrYxqUVne3tU_Q'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your friendly bot. How can I assist you?')


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('You can use the following commands:\n/start - Start the bot\n/help - Get help information')


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
