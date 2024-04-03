import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    update.message.reply_text('مرحبًا! هذا البوت الخاص بك.')

def help_command(update, context):
    update.message.reply_text('هذه رسالة المساعدة.')

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("6899925099:AAG9i25hphBfUBy8iU7o_uGiaw1z65F5n38", use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()
updater.idle()
