import telebot
from . import bot
from .telegram_bot import telegram_bot, WEBHOOK_URL_PATH, WEBHOOK_URL_BASE
from flask import request, abort
from time import sleep

# Remove webhook, it fails sometimes the set if there is a previous webhook
telegram_bot.remove_webhook()

# Wait
sleep(1)

# Set webhook
telegram_bot.set_webhook(WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

@bot.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        telegram_bot.process_new_updates([update])
        return ''
    else:
        return abort(403)
